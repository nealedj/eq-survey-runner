from flask import Blueprint, request, current_app
from flask_themes2 import render_theme_template
from flask_login import current_user
from flask_wtf.csrf import CSRFError

from structlog import get_logger
from ua_parser import user_agent_parser

from app.authentication.invalid_token_exception import InvalidTokenException
from app.authentication.no_token_exception import NoTokenException
from app.globals import get_metadata
from app.libs.utils import convert_tx_id
from app.submitter.submission_failed import SubmissionFailedException

logger = get_logger()

errors_blueprint = Blueprint('errors', __name__)


class MultipleSurveyError(Exception):
    pass


@errors_blueprint.after_request
def add_cache_control(response):
    response.cache_control.no_cache = True
    return response


@errors_blueprint.app_errorhandler(401)
@errors_blueprint.app_errorhandler(NoTokenException)
def unauthorized(error=None):
    log_exception(error, 401)
    return render_theme_template('default', 'session-expired.html'), 401


@errors_blueprint.app_errorhandler(InvalidTokenException)
def forbidden(error=None):
    log_exception(error, 403)
    return _render_error_page(403)


@errors_blueprint.app_errorhandler(SubmissionFailedException)
def service_unavailable(error=None):
    log_exception(error, 503)
    return _render_error_page(503)


@errors_blueprint.app_errorhandler(MultipleSurveyError)
def multiple_survey_error(error=None):
    log_exception(error, 200)
    return render_theme_template('default', 'multiple_survey.html')


@errors_blueprint.app_errorhandler(CSRFError)
def csrf_exception(error):
    log_exception(error, error.code)
    return render_theme_template('default', 'csrf_exception.html'), error.code


@errors_blueprint.app_errorhandler(Exception)
def internal_server_error(error=None):
    log_exception(error, 500)
    return _render_error_page(500)


@errors_blueprint.app_errorhandler(403)
@errors_blueprint.app_errorhandler(404)
def http_exception(error):
    log_exception(error, error.code)
    return _render_error_page(error.code)


def log_exception(error, status_code):
    if error:
        logger.error('an error has occurred', exc_info=error, url=request.url, status_code=status_code)
    else:
        logger.error('an error has occurred', url=request.url, status_code=status_code)


def _render_error_page(status_code):
    tx_id = get_tx_id()
    user_agent = user_agent_parser.Parse(request.headers.get('User-Agent', ''))

    return render_theme_template('default', 'errors/error.html',
                                 status_code=status_code,
                                 analytics_ua_id=current_app.config['EQ_UA_ID'],
                                 ua=user_agent, tx_id=tx_id), status_code


def get_tx_id():
    tx_id = None
    metadata = get_metadata(current_user)
    if metadata:
        tx_id = convert_tx_id(metadata["tx_id"])
    return tx_id
