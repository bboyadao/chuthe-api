#!/bin/bash
python manage.py collectstatic --noinput
python manage.py createcachetable
python manage.py migrate
echo "startting appication"
daphne -b 0.0.0.0 -p 8000 chuthe.asgi:application

