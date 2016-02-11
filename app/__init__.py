from flask.ext.babel import Babel
import pytz
from flask import Flask
from app.libs.utils import get_locale
from healthcheck import HealthCheck, EnvironmentDump
from flaskext.markdown import Markdown

from app.submitter.submitter import Submitter
import logging

DISPLAY_DATETIME_FORMAT = '%A %d %B %Y at %H:%M'
DATETIME_FORMAT = "%Y-%m-%dT%H:%M:%S.%fZ"
EUROPE_LONDON = pytz.timezone("Europe/London")


def rabbitmq_available():
    submitter = Submitter()
    if submitter.send_test():
        return True, "rabbit mq ok"
    else:
        return False, "rabbit mq unavailable"


def get_git_revision():
    try:
        revision_log = open("revision.log")
        revision = revision_log.readlines()
        revision_log.close()
        return True, revision
    except FileNotFoundError:
        logging.exception("Git revision file missing")
        return False, "Git revision not available"

GIT_REVISION = get_git_revision()


def git_revision():
    return GIT_REVISION


def create_app(config_name):
    application = Flask(__name__, static_url_path='/static')
    headers = {'Content-Type': 'application/json', 'Cache-Control': 'no-cache, no-store, must-revalidate', 'Pragma': 'no-cache'}
    application.healthcheck = HealthCheck(application, '/healthcheck', success_headers=headers, failed_headers=headers)
    application.healthcheck.add_check(rabbitmq_available)
    application.healthcheck.add_check(git_revision)
    application.babel = Babel(application)
    application.babel.localeselector(get_locale)
    application.jinja_env.add_extension('jinja2.ext.i18n')
    application.envdump = EnvironmentDump(application, '/environment')
    Markdown(application, extensions=['gfm'])

    from .main import main as main_blueprint
    application.register_blueprint(main_blueprint)
    main_blueprint.config = application.config.copy()
    return application
