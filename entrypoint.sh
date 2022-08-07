#!/bin/bash
python manage.py migrate
python manage.py collectstatic --noinput
python manage.py createcachetable
echo "startting appication"
daphne -b 0.0.0.0 -p 8000 chuthe.asgi:application