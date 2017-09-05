import json
import os
import requests

from structlog import get_logger
from werkzeug.exceptions import NotFound

from app.setup import cache

logger = get_logger()

DEFAULT_SCHEMA_DIR = 'data'
DEFAULT_LANGUAGE_CODE = 'en'


def load_schema_from_metadata(metadata):
    if metadata.get('survey_url'):
        return load_schema_from_url(metadata['survey_url'], metadata.get('language_code'))

    return load_schema_from_params(
        metadata['eq_id'],
        metadata['form_type'],
        metadata.get('language_code'),
    )


@cache.memoize()
def load_schema_from_params(eq_id, form_type, language_code=DEFAULT_LANGUAGE_CODE):
    return load_schema_file("{}_{}.json".format(eq_id, form_type), language_code)


def load_schema_file(schema_file, language_code=None):
    """
    Load a schema, optionally for a specified language.
    :param schema_file: The name of the schema e.g. census_household.json
    :param language_code: ISO 2-character code for language e.g. 'en', 'cy'
    """
    language_code = language_code or DEFAULT_LANGUAGE_CODE
    schema_path = get_schema_file_path(schema_file, language_code)

    if language_code != DEFAULT_LANGUAGE_CODE and not os.path.exists(schema_path):
        logger.info("couldn't find requested language schema, falling back to 'en'",
                    schema_file=schema_file, language_code=language_code, schema_path=schema_path)
        schema_path = get_schema_file_path(schema_file, DEFAULT_LANGUAGE_CODE)

    logger.info("loading schema", schema_file=schema_file, language_code=language_code, schema_path=schema_path)

    try:
        with open(schema_path, encoding="utf8") as json_data:
            return json.load(json_data)

    except FileNotFoundError as e:
        logger.error("no schema file exists", filename=schema_path)
        raise e


@cache.memoize()
def load_schema_from_url(survey_url, language_code):
    logger.info("loading schema from URL", survey_url=survey_url, language_code=language_code)

    constructed_survey_url = "{}?language={}".format(survey_url, language_code)

    req = requests.get(constructed_survey_url)
    schema_response = req.content.decode()

    if req.status_code == 404:
        logger.error("no schema exists", survey_url=constructed_survey_url)
        raise NotFound

    return json.loads(schema_response)


def get_schema_definition_path(schema_dir=DEFAULT_SCHEMA_DIR):
    return os.path.join(schema_dir, "schema/schema_v1.json")


def get_schema_path(schema_dir=DEFAULT_SCHEMA_DIR, language_code=DEFAULT_LANGUAGE_CODE):
    return os.path.join(schema_dir, language_code)


def get_schema_file_path(schema_file, language_code=DEFAULT_LANGUAGE_CODE):
    schema_dir = get_schema_path(language_code=language_code)
    return os.path.join(schema_dir, schema_file)
