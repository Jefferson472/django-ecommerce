celery:
	celery -A setup --workdir src  worker -l info -P gevent

flower:
	# localhost:5555
	celery -A setup --workdir src flower -P gevent

migrations:
	python3 src/manage.py makemigrations
	python3 src/manage.py migrate

pip:
	pip install -r requirements.txt
	pip freeze > requirements.txt

freeze:
	pip freeze > requirements.txt

rabbit:
	docker run -d --rm --hostname myhost --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:3.10-management

runserver:
	python3 src/manage.py runserver

shell:
	python3 src/manage.py shell

venv:
	source lvenv/bin/activate

venv-d:
	source lvenv/Scripts/deactivate.bat

venv-venv:
	virtualenv lvenv