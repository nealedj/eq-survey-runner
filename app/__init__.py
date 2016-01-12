import os
from datetime import timedelta, datetime
from flask.ext.babel import Babel
import pytz
from flask import Flask, render_template
from config import configs
from app.libs.utils import get_locale
from healthcheck import HealthCheck, EnvironmentDump

DISPLAY_DATETIME_FORMAT = '%A %d %B %Y at %H:%M'
DATETIME_FORMAT = "%Y-%m-%dT%H:%M:%S.%fZ"
EUROPE_LONDON = pytz.timezone("Europe/London")


def create_app(config_name):
    application = Flask(__name__)
    application.healthcheck = HealthCheck(application, '/healthcheck')
    application.babel = Babel(application)
    application.babel.localeselector(get_locale)
    application.jinja_env.add_extension('jinja2.ext.i18n')
    application.envdump = EnvironmentDump(application, '/environment')

    from .main import main as main_blueprint
    application.register_blueprint(main_blueprint)
    main_blueprint.config = application.config.copy()
    return application
