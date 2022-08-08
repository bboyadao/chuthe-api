"""
This is the common settings for project.
"""

import logging
import os
from pathlib import Path
from django.urls import reverse_lazy
from firebase_admin import initialize_app
from ..logging import LOGGING
from logging import config

LOGGING_CONFIG = None
config.dictConfig(LOGGING)
LOGGER = logging.getLogger("my_json")

SITE_ID = 1
BASE_DIR = Path(__file__).resolve().parent.parent

PROJECT_NAME = "chuthe"

ENVS = ["PROD", "STAGING", "DEV", "LOCAL"]

ENV = os.environ.get("CHUTHE_ENV")

SECRET_KEY = os.getenv("SECRET_KEY")

CELERY_CACHE_BACKEND = "default"
CELERY_TASK_SERIALIZER = "json"
CELERY_RESULT_SERIALIZER = "json"
CELERY_ENABLE_UTC = True
CELERY_RESULT_BACKEND = "django-db"
DJANGO_CELERY_RESULTS_TASK_ID_MAX_LENGTH = 191

ALLOWED_HOSTS = ["*"]

AUTH_APPS = [
    "rest_framework_simplejwt.token_blacklist",
    "oauth2_provider",
    "rest_framework.authtoken",
    "dj_rest_auth",
    "allauth",
    "allauth.account",
    "dj_rest_auth.registration",
    "allauth.socialaccount",
    "allauth.socialaccount.providers.facebook",
]

DOCS_APPS = ["drf_spectacular",
             "drf_spectacular_sidecar"]

CELERY_APPS = ["django_celery_results",
               "django_celery_beat"]

LIB_APPS = ["rest_framework",
            "phonenumber_field",
            "corsheaders",
            "fcm_django",
            "actstream",
            ]

EXTERNAL_APPS = LIB_APPS + CELERY_APPS + AUTH_APPS + DOCS_APPS

DJANGO_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.sites"
]

INTERNAL_APPS = [
    "user.apps.UserConfig",
    "apps.apps.AppsConfig",
    "company.apps.CompanyConfig",
    "alias.apps.AliasConfig",
    "nof.apps.NofConfig",
]

AUTH_USER_MODEL = "user.User"

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "chuthe.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "chuthe.wsgi.application"

STORAGE_DIR = "storage"

CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.db.DatabaseCache",
        "LOCATION": "django_cache",
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME":
            "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME":
            "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME":
            "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME":
            "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True

STATIC_URL = "static/"

STATIC_ROOT = os.path.join(STORAGE_DIR, "staticfiles")

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

REST_FRAMEWORK = {
    "TEST_REQUEST_DEFAULT_FORMAT": "json",
    "DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema",
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework.authentication.SessionAuthentication",
        "rest_framework.authentication.BasicAuthentication",
        "dj_rest_auth.jwt_auth.JWTCookieAuthentication",
    ]
}
REST_USE_JWT = True
JWT_AUTH_COOKIE = "CHUTHE_BOOTSTRAP"
AUTHENTICATION_BACKENDS = [
    "user.auth.ChutheAuth"
]

SPECTACULAR_SETTINGS = {
    "PREPROCESSING_HOOKS": ["docs.hooks.preprocessing_filter_spec"],
    'TITLE': "ChuThe's Api Documents",
    'DESCRIPTION': "This describe specs i/o modules only for internal team.",
    'VERSION': '0.1.0',
    'SERVE_INCLUDE_SCHEMA': True,
    'REDOC_DIST': 'SIDECAR',
    "EXCLUDE_PATH": [
        reverse_lazy("schema")
    ],
    'EXTENSIONS_INFO': {
        "x-logo": {
            "url": "https://raw.githubusercontent.com/bboyadao/static_me/main/imgs/chuthe/logo1.png",
            "backgroundColor": "#FFFFFF",
            "altText": "Nice NIce Logo"
        },
        "x-meta":
            {
                "keywords": "documentation, operation, example",
                "image": "https://raw.githubusercontent.com/bboyadao/static_me/main/imgs/chuthe/favicon.png"
            }
    },

}

DOCS_TAG = {
    "ADMINSTRATOR": [],
    "USER": [],
    "STAFF": [],
    "PUBLIC": [],
}

PUSH_NOTIFICATIONS_SETTINGS = {
    "FCM_API_KEY": "[your api key]",
}

FIREBASE_APP = initialize_app()

FCM_DJANGO_SETTINGS = {
    # an instance of firebase_admin.App to be used as default for all fcm-django requests
    # default: None (the default Firebase app)
    "DEFAULT_FIREBASE_APP": None,
    # default: _('FCM Django')
    "APP_VERBOSE_NAME": "Chuthe-PROD",
    # true if you want to have only one active device per registered user at a time
    # default: False
    "ONE_DEVICE_PER_USER": False,
    # devices to which notifications cannot be sent,
    # are deleted upon receiving error response from FCM
    # default: False
    "DELETE_INACTIVE_DEVICES": True,
    # Transform create of an existing Device (based on registration id) into
    # an update. See the section
    # "Update of device with duplicate registration ID" for more details.
    "UPDATE_ON_DUPLICATE_REG_ID": True,
}
