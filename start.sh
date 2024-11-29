#!/bin/bash
python manage.py migrate  # Run database migrations
python manage.py collectstatic --noinput  # Collect static files
gunicorn weather.wsgi:application  # Start the Gunicorn server
