import time

from celery import shared_task
from user.models import User


@shared_task
def test_user(data, colazo):
    for i in range(100):
        print("called from view with apply_async")
        time.sleep(1)
    return 1


@shared_task
def add():
    users = User.objects.all()
    return [i.username for i in users]
