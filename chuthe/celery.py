import os
import sys
from datetime import timedelta

from celery import Celery

from chuthe.settings.commons import PROJECT_NAME
from chuthe import celery_config

env = os.getenv("CHUTHE_ENV")
if env is None:
    sys.exit(1)

# logger.info(f"Running on django setting file's: {PROJECT_NAME}.settings.{env.lower()}")

try:
    exec(f"from .settings import {env.lower()}")
except ImportError as e:
    raise ModuleNotFoundError(f"Can not dertimined environment you are in: {env}, PLEASE export it")

os.environ.setdefault("DJANGO_SETTINGS_MODULE", f"{PROJECT_NAME}.settings.{env.lower()}")
app = Celery(PROJECT_NAME)
app.config_from_object(celery_config)
app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print(f"Request: {self.request!r}")

# app.conf.beat_schedule = {
#     'every-minute': {
#         'task': 'user.tasks.add',
#         'schedule': timedelta(seconds=5),
#         'args': ()
#     },
# }
