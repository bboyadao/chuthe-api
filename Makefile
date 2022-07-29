init:
	export CHUCHUTHE_ENV="LOCAL"

b:
	docker build -t chuthe:latest -f Dockerfile .
	docker tag chuthe:latest 0x7c/chuthe:latest
p:
	docker push 0x7c/chuthe

r:
	python manage.py runserver

ru:
	python manage.py runserver_plus 0.0.0.0:8000 --keep-meta-shutdown

sh:
	python manage.py shell_plus

cl:
	rm ./storage/db.sqlite3
	find . -path "*/migrations/*.py" -not -name "__init__.py" -delete
	find . -path "*/migrations/*.pyc"  -delete
mk:
	python manage.py makemigrations

mi:
	python manage.py migrate

cac:
	python manage.py createcachetable

su:
	echo "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser('admin', 'admin@gmail.com', 'admin123')" | python manage.py shell

mock:
	python manage.py mock_alias
#	python manage.py shell < user/mocks.py
#	python manage.py shell < heo/mocks.py

