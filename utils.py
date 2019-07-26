import logging
import logging.config
import requests
from flask import current_app as app


def config_logger(app):
    logging.config.dictConfig(app.config.get('LOGGING_CONFIG'))
    logger = logging.getLogger(app.config.get("DEFAULT_LOGGER_NAME"))
    app.logger.addHandler(logger)
    app.logger.info("logger configured")


def get_google_provider_cfg():
    return requests.get(app.config.get('GOOGLE_DISCOVERY_URL')).json()
