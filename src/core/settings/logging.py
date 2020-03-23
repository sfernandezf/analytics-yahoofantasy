import os
import logging


LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'standard': {
            'format': "[%(asctime)s] %(levelname)s [%(name)s:%(lineno)s] "
                      "%(message)s",
            'datefmt': "%d%b %H:%M:%S"
        },
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'standard',
        },
    },
    'loggers': {
        '': {
            'level': os.environ.get('LOGGING_LEVEL', 'INFO'),
            'handlers': ['console'],
        },
        'django': {
            'level': os.environ.get('DJANGO_LOGGING_LEVEL', 'ERROR'),
            'handlers': ['console'],
        },
    },
}

logging.basicConfig(
    level=getattr(logging, os.environ.get('LOGGING_LEVEL', 'INFO'), 20),
    format="[%(levelname)s %(asctime)s] %(name)s: %(message)s",
)
