migrations:
	python3 src/manage.py makemigrations
	python3 src/manage.py migrate

pip:
	pip install -r requirements.txt
	pip freeze > requirements.txt

runserver:
	python3 src/manage.py runserver

shell:
	python3 src/manage.py shell

venv:
	source venv/bin/activate

venv-d:
	source venv/Scripts/deactivate.bat

venv-venv:
	virtualenv venv