
docker-compose up --build -d
docker-compose exec backend python manage.py migrate --noinput
docker-compose exec backend python manage.py collectstatic --noinput

echo 'Create a user for your application '

docker-compose exec backend python manage.py createsuperuser

echo 'all operation done successfully!!!'