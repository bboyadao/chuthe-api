from .commons import *  # noqa

DATABASE_NAME = os.getenv("DATABASE_NAME")
DATABASE_URL = os.getenv("DATABASE_URL")
DATABASE_PORT = os.getenv("DATABASE_PORT")
DATABASE_USER = os.getenv("DATABASE_USER")
DATABASE_PASSWORD = os.getenv("DATABASE_PASSWORD")

SECRET_KEY = os.getenv("SECRET_KEY")
DEBUG = False

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": DATABASE_NAME,
        "USER": DATABASE_USER,
        "PASSWORD": DATABASE_PASSWORD,
        "HOST": DATABASE_URL,
        "PORT": DATABASE_PORT,
        "TEST": {
            "NAME": "testdb"
        },
    },
}

INSTALLED_APPS = DJANGO_APPS + EXTERNAL_APPS + INTERNAL_APPS
