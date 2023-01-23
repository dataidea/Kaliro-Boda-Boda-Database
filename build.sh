#!/usr/bin/env bash
# exit on error
set -o errexit

pip install --upgrade pip

poetry install

python manage.py collectstatic --no-input
python manage.py makemigrations
python manage.py migrate

pip install --force-reinstall -U setuptools

if [[ $CREATE_SUPERUSER ]];
then
  python world_champ_2022/manage.py createsuperuser --no-input