from celery import shared_task


@shared_task
def test_user():
    "AAAAA"
    print("plplplplp")
    return 1

