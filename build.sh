#!/usr/bin/env bash
# exit on error
set -o errexit


echo "-----> Poetry install"
poetry install --without dev --no-root --no-interaction
echo "-----> Poetry done"

echo "-----> Running manage.py check --deploy --fail-level WARNING"
poetry run src/manage.py check --deploy --fail-level WARNING

echo "-----> Running collectstatic"
poetry run src/manage.py collectstatic --no-input

echo "-----> Running manage.py migrate"
poetry run src/manage.py migrate --noinput


echo "-----> Post-compile done 🎈✨🎉"
