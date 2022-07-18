"""
This is the common settings for project.
"""
import os
from pathlib import Path

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
APPEND_SLASH = True

AUTH_APPS = [
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
            "corsheaders"]

EXTERNAL_APPS = LIB_APPS + CELERY_APPS + AUTH_APPS + DOCS_APPS

DJANGO_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]

INTERNAL_APPS = [
    "user.apps.UserConfig",
    "apps.apps.AppsConfig",
    "company.apps.CompanyConfig",
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
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework.authentication.SessionAuthentication",
        "rest_framework.authentication.BasicAuthentication",
        "dj_rest_auth.jwt_auth.JWTCookieAuthentication",
    ]
}
REST_USE_JWT = True

AUTHENTICATION_BACKENDS = [
    "user.auth.ChutheAuth"
]

SPECTACULAR_SETTINGS = {
    "PREPROCESSING_HOOKS": ["docs.preprocessing_filter_spec"],

    'TITLE': "ChuThe's Api Documents",
    'DESCRIPTION': "This describe specs i/o modules only for internal team.",
    'VERSION': '0.1.0',
    'SERVE_INCLUDE_SCHEMA': False,
    # OTHER SETTINGS
    'REDOC_DIST': 'SIDECAR',
}
