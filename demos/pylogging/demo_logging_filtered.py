"""
Voir : https://docs.python.org/3/library/logging.config.html#configuration-dictionary-schema
"""

import logging
import logging.config

class NonErrorFilter(logging.Filter):
    def filter(self, record: logging.LogRecord):
        return record.levelno <= logging.INFO

logging_config = {
    'version': 1,
    'disable_existing_loggers': False,

    'formatters': {
        'daily': {
            'format': '%(asctime)s - %(levelname)s - %(message)s',
            'datefmt': '%H:%M:%S',
        },
        'complete': {
            'format': '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        }
    },

    'filters': {
        'info_only': {
            '()': NonErrorFilter,
        }
    },

    'handlers': {
        'stdout': {
            'class': 'logging.StreamHandler',
            'formatter': 'daily',
            'filters': ['info_only',],
            'stream': 'ext://sys.stdout',
        },
        'file': {
            'class': 'logging.FileHandler',
            'formatter': 'complete',
            'level': 'ERROR',
            'filename': "file.log",
        },
    },

    'loggers': {
        'root': {
            'level': 'INFO', 'handlers': ['stdout', 'file', ],
        },
    }
}


logging.config.dictConfig(logging_config)
logger = logging.getLogger(__name__)

logger.debug('Un debug')
logger.info('Une info')
logger.warning("Un warning")
logger.error("Une erreur")
logger.critical('Critique')
