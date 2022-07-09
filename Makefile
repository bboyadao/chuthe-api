#init: b p

#b:
#	docker build -t chuthe:latest -f Dockerfile .
#	docker tag chuthe:latest 0x7c/chuthe:latest
p:
	docker push 0x7c/chuthe
r:
	python manage.py runserver
mi:
	python manage.py migrate
mk:
	python manage.py makemigrations
sh:
	python manage.py shell_plus