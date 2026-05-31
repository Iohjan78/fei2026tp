#!/bin/bash
set -e

cd /app/backend

if [ ! -f manage.py ]; then
    django-admin startproject fei2026tp .
fi

python manage.py makemigrations
python manage.py migrate

python manage.py createsuperuser --noinput || true

python manage.py runserver 0.0.0.0:8000
