celery:
	celery -A setup --workdir src  worker -l info

flower:
	# localhost:5555
	celery -A setup --workdir src flower

migrations:
	python3 src/manage.py makemigrations
	python3 src/manage.py migrate

pip:
	pip install -r requirements.txt
	pip freeze > requirements.txt

rabbit:
	docker run -d --hostname vhost --name rabbit -p 5672:5672 rabbitmq

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