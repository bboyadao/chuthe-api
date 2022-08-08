LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
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
            '()': 'json_log_formatter.VerboseJSONFormatter',
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
            'formatter': 'simple'
        },
        'json_file': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': './my-log.json',
            'formatter': 'json',
            'maxBytes': 1024*1024*15,  # 15MB
            'backupCount': 10,
        },

    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'propagate': True,
        },
        'my_json': {
            'handlers': ['json_file'],
            'level': 'INFO',
        }

    }
}
