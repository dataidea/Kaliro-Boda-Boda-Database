#!/usr/bin/env bash
# exit on error
set -o errexit

pip install --upgrade pip

poetry install

python manage.py collectstatic --no-input
python manage.py createsuperuser --username=jumashafara --email=jumashafara0@gmail.com --password=chappie256
python manage.py makemigrations
python manage.py migrate

pip install --force-reinstall -U setuptools