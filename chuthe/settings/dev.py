from .commons import *  # noqa

DATABASES = {
	'default': {
		'ENGINE': 'django.db.backends.sqlite3',
		'NAME': os.path.join(STORAGE_DIR, 'db.sqlite3'),
	}
}
DEBUG = True
INSTALLED_APPS = DJANGO_APPS + EXTERNAL_APPS + INTERNAL_APPS
