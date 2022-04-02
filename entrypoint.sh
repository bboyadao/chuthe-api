#!/bin/bash
# exec python manage.py createcachetable
python manage.py collectstatic --noinput
echo "startting appication"
daphne chuthe.asgi:application

