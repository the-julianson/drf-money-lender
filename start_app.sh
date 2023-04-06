#!/usr/bin/env bash
# exit on error
set -o errexit
set -o pipefail
set -o nounset
echo "Running migrations, creating super user, and collecting static"
python manage.py migrate
#python manage.py createsuperuser --noinput --email $DJANGO_SUPERUSER_EMAIL || echo "Superuser already exists"
echo "Ready for app server"
#gunicorn core.wsgi:application --bind 0.0.0.0:$PORT
python manage.py runserver 0.0.0.0:8000