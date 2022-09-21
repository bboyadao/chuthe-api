import os


cache_backend = "default"
task_serializer = "json"
result_serializer = "json"
enable_utc = True
result_backend = "django-db"
worker_send_task_event = False
task_ignore_result = True
task_time_limit = 190
task_soft_time_limit = 180
task_acks_late = True
worker_prefetch_multiplier = 1

broker_schema = os.getenv("BROKER_SCHEMA")
broker_user = os.getenv("BROKER_USER")
broker_password = os.getenv("BROKER_PASSWORD")
broker_host = os.getenv("BROKER_HOST")
broker_port = os.getenv("BROKER_PORT")

AMQP_BROKER_URL = (
            f"{broker_schema}://{broker_user}:{broker_password}@{broker_host}:{broker_port}"
            )

broker_url = AMQP_BROKER_URL
