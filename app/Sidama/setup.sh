#!/usr/bin/env bash

until nc -z ${POSTGRES_HOST} 5432; do
    echo "$(date) - waiting for postgres..."
    sleep 1
done

./manage.py migrate --noinput
./manage.py collectstatic --noinput
./manage.py loaddata ./SidamaApp/data/db.json
exec gunicorn -w 4 -b :8000 Sidama.wsgi
