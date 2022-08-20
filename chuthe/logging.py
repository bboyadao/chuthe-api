from json_log_formatter import VerboseJSONFormatter


LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'verbose': {
            'format': '{levelname} {asctime} {module} {process:d} {thread:d} {message}',
            'style': '{',
        },
        'simple': {
            'format': '{levelname} {message}',
            'style': '{',
        },
        'json': {
            '()': 'chuthe.logging.CustomJsonLogFormatter',
        },
    },
    'filters': {
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
    },
    'handlers': {
        'console': {
            'level': 'INFO',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
            'formatter': 'json'
        },
        # 'json_file': {
        #     'level': 'INFO',
        #     'class': 'logging.handlers.RotatingFileHandler',
        #     'filename': './logs/api/log.json',
        #     'formatter': 'json',
        #     'maxBytes': 1024 * 1024 * 15,  # 15MB
        #     'backupCount': 10,
        # },

    },
    'loggers': {
        'chuthe': {
            'handlers': ['console'],
            "propagate": True,
            'level': 'DEBUG',
        }

    }
}


class CustomJsonLogFormatter(VerboseJSONFormatter):
    def json_record(self, message, extra, record):
        extra['levelname'] = record.levelname
        extra['name'] = record.name
        extra['pathname'] = record.pathname
        extra['process'] = record.process
        extra['processName'] = record.processName
        if hasattr(record, 'stack_info'):
            extra['stack_info'] = record.stack_info
        else:
            extra['stack_info'] = None
        # extra['thread'] = record.thread
        # extra['threadName'] = record.threadName
        # extra['filename'] = record.filename
        # extra['funcName'] = record.funcName
        # extra['lineno'] = record.lineno
        # extra['module'] = record.module

        return super(VerboseJSONFormatter, self).json_record(message, extra, record)
