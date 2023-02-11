#!/bin/bash

docker-compose up --build -d
docker-compose exec backend python manage.py migrate --noinput
docker-compose exec backend python manage.py collectstatic --noinput

