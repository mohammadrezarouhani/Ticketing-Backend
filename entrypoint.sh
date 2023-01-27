#!/bin/bash

docker-compose up --build -d
docker-compose exec backend python manage.py migrate --on-input
docker-compose exec backend python manage.py collectstatic --on-input

