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
LOGGER = logging.getLogger("chuthe")
SITE_ID = 1
BASE_DIR = Path(__file__).resolve().parent.parent

PROJECT_NAME = "chuthe"

ENVS = ["PROD", "STAGING", "DEV"]

ENV = os.environ.get("CHUTHE_ENV")

SECRET_KEY = os.getenv("SECRET_KEY")

DJANGO_CELERY_RESULTS_TASK_ID_MAX_LENGTH = 191

ALLOWED_HOSTS = ["*"]

AUTH_APPS = [
    "rest_framework_simplejwt.token_blacklist",
    "oauth2_provider",
    "rest_framework.authtoken",
    "dj_rest_auth",
    "dj_rest_auth.registration",
    "allauth",
    "allauth.account",
    "allauth.socialaccount",
    "allauth.socialaccount.providers.facebook",
    "allauth.socialaccount.providers.google",
    "allauth.socialaccount.providers.linkedin_oauth2",
    "allauth.socialaccount.providers.github",
    "allauth.socialaccount.providers.twitter",
]

DOCS_APPS = ["drf_spectacular",
             "drf_spectacular_sidecar"]

CELERY_APPS = ["django_celery_results",
               "django_celery_beat"]

LIB_APPS = ["rest_framework",
            "django_filters",
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
    "manager.apps.ManagerConfig",
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
    "chuthe.middlewares.supervisor.ChutheIOMiddleware",
]

ROOT_URLCONF = "chuthe.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, "templates")],
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

USER_TIME_ZONE = "Asia/Ho_Chi_Minh"

LANGUAGE_CODE = "en-us"
# LANGUAGE_CODE = 'vi'

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
    ],
}
REST_USE_JWT = True
JWT_AUTH_COOKIE = "CHUTHE_BOOTSTRAP"
AUTHENTICATION_BACKENDS = [
    "user.auth.ChutheAuth"
]

REST_AUTH = {
    "LOGIN_SERIALIZER": "chuthe.auth.serializers.LoginSerializer",
    # 'LOGIN_SERIALIZER': 'dj_rest_auth.serializers.LoginSerializer',
    'TOKEN_SERIALIZER': 'dj_rest_auth.serializers.TokenSerializer',
    'JWT_SERIALIZER': 'dj_rest_auth.serializers.JWTSerializer',
    'JWT_SERIALIZER_WITH_EXPIRATION': 'dj_rest_auth.serializers.JWTSerializerWithExpiration',
    'JWT_TOKEN_CLAIMS_SERIALIZER': 'rest_framework_simplejwt.serializers.TokenObtainPairSerializer',
    'USER_DETAILS_SERIALIZER': 'dj_rest_auth.serializers.UserDetailsSerializer',
    'PASSWORD_RESET_SERIALIZER': 'dj_rest_auth.serializers.PasswordResetSerializer',
    'PASSWORD_RESET_CONFIRM_SERIALIZER': 'dj_rest_auth.serializers.PasswordResetConfirmSerializer',
    'PASSWORD_CHANGE_SERIALIZER': 'dj_rest_auth.serializers.PasswordChangeSerializer',

    # 'REGISTER_SERIALIZER': 'dj_rest_auth.registration.serializers.RegisterSerializer',
    'REGISTER_SERIALIZER': 'chuthe.auth.serializers.RegisterSerializer',

    'REGISTER_PERMISSION_CLASSES': ('rest_framework.permissions.AllowAny',),

    'TOKEN_MODEL': 'rest_framework.authtoken.models.Token',
    'TOKEN_CREATOR': 'dj_rest_auth.utils.default_create_token',

    'PASSWORD_RESET_USE_SITES_DOMAIN': False,
    'OLD_PASSWORD_FIELD_ENABLED': False,
    'LOGOUT_ON_PASSWORD_CHANGE': False,
    'SESSION_LOGIN': True,
    'USE_JWT': False,

    'JWT_AUTH_COOKIE': None,
    'JWT_AUTH_REFRESH_COOKIE': None,
    'JWT_AUTH_REFRESH_COOKIE_PATH': '/',
    'JWT_AUTH_SECURE': False,
    'JWT_AUTH_HTTPONLY': True,
    'JWT_AUTH_SAMESITE': 'Lax',
    'JWT_AUTH_RETURN_EXPIRATION': False,
    'JWT_AUTH_COOKIE_USE_CSRF': False,
    'JWT_AUTH_COOKIE_ENFORCE_CSRF_ON_UNAUTHENTICATED': False,
}

SPECTACULAR_SETTINGS = {
    "PREPROCESSING_HOOKS": ["docs.hooks.preprocessing_filter_spec"],
    'TITLE': "ChuThe's Api Documents",
    'DESCRIPTION': "This describe specs i/o modules only for internal team.",
    'VERSION': '0.1.0',
    'SERVE_INCLUDE_SCHEMA': True,
    'SERVE_PERMISSIONS': ['rest_framework.permissions.IsAuthenticated'],
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

DOCS_GROUP = {
    "ADMINISTRATOR": [],
    "USER": [],
    "ALIAS": [],
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

SOCIALACCOUNT_PROVIDERS = {

    'google': {
        'APP': {
            'client_id': os.getenv("GOOGLE_CLIENT_ID"),
            'secret': os.getenv("GOOGLE_CLIENT_SEC"),
            'key': ''
        }
    },
    'linkedin': {
        'SCOPE': [
            'r_basicprofile',
            'r_emailaddress',
        ],
        'PROFILE_FIELDS': [
            'id',
            'first-name',
            'last-name',
            'email-address',
            'picture-url',
            'public-profile-url',
        ]
    }
}

ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_EMAIL_VERIFICATION = "mandatory"
ACCOUNT_AUTO_SIGNUP = True
ACCOUNT_EMAIL_CONFIRMATION_HMAC = True
ACCOUNT_EMAIL_CONFIRMATION_EXPIRE_DAYS = 1
ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_AUTHENTICATION_METHOD = "username"
ACCOUNT_EMAIL_CONFIRMATION_COOLDOWN = 180


