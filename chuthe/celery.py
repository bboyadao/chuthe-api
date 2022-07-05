import os
import sys
from celery import Celery
from chuthe.settings.commons import PROJECT_NAME

env = os.getenv("CHUTHE_ENV")
if env is None:
    sys.exit(1)

print(f"Running on django setting file's: {PROJECT_NAME}.settings.{env.lower()}")

try:
    exec(f"from .settings import {env.lower()}")
except ImportError as e:
    raise ModuleNotFoundError(f"Can not dertimined environment you are in: {env}, PLEASE export it")

os.environ.setdefault("DJANGO_SETTINGS_MODULE", f"{PROJECT_NAME}.settings.{env.lower()}")
app = Celery(PROJECT_NAME)
app.config_from_object("django.conf:settings")
app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):

    print(f"Request: {self.request!r}")
