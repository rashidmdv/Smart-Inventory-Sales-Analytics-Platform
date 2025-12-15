import os
from . import BASE_DIR
from django.utils.timezone import localtime
import logging



LOG_BASE_DIR = os.path.join(BASE_DIR, "logs")

DJANGO_LOG_DIR = os.path.join(LOG_BASE_DIR, "django")
ERROR_LOG_DIR = os.path.join(LOG_BASE_DIR, "errors")
STUDENTS_LOG_DIR = os.path.join(LOG_BASE_DIR, "students")
ACCOUNTS_LOG_DIR = os.path.join(LOG_BASE_DIR, "accounts")


# Auto create all folders safely
for path in [DJANGO_LOG_DIR, ERROR_LOG_DIR, STUDENTS_LOG_DIR, ACCOUNTS_LOG_DIR]:
    os.makedirs(path, exist_ok=True)


def django_time(*args):
    return localtime().timetuple()

logging.Formatter.converter = django_time


LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,

    "formatters": {
        "simple": {
            "format": "[%(asctime)s] %(levelname)s %(message)s",
        },
        "verbose": {
            "format": "[%(asctime)s] %(levelname)s [%(name)s:%(lineno)d] %(message)s",
        },
    },

    "handlers": {
        #  Console
        "console": {
            "class": "logging.StreamHandler",
            "formatter": "simple",
        },

        #  Django main daily log
        "django_file": {
            "level": "INFO",
            "class": "logging.handlers.TimedRotatingFileHandler",
            "filename": os.path.join(DJANGO_LOG_DIR, "django.log"),
            "when": "midnight",
            "interval": 1,
            "backupCount": 7,
            "formatter": "verbose",
        },

        #  Error-only daily log
        "error_file": {
            "level": "ERROR",
            "class": "logging.handlers.TimedRotatingFileHandler",
            "filename": os.path.join(ERROR_LOG_DIR, "errors.log"),
            "when": "midnight",
            "interval": 1,
            "backupCount": 15,
            "formatter": "verbose",
        },


        #  Accounts daily log
        "accounts_file": {
            "level": "INFO",
            "class": "logging.handlers.TimedRotatingFileHandler",
            "filename": os.path.join(ACCOUNTS_LOG_DIR, "accounts.log"),
            "when": "midnight",
            "interval": 1,
            "backupCount": 7,
            "formatter": "verbose",
        },
        
    },

    "root": {
        "handlers": ["console", "django_file", "error_file"],
        "level": "INFO",
    },

    "loggers": {
        #  Django internal logs
        "django": {
            "handlers": ["console", "django_file", "error_file"],
            "level": "INFO",
            "propagate": False,
        },

        #  Only request errors
        "django.request": {
            "handlers": ["error_file"],
            "level": "ERROR",
            "propagate": False,
        },

        #  Accounts module logs
        "apps.accounts": {
            "handlers": ["accounts_file", "console"],
            "level": "INFO",
            "propagate": False,
        },

    },

}



