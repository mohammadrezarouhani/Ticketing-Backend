from ticketing_backend.settings.settings import *


env=environ.Env()
env.read_env(os.path.join(BASE_DIR,'environment','prod.env'))

SECRET_KEY = env('SECRET_KEY')
DEBUG = bool(int(env('DEBUG')))

ALLOWED_HOSTS = env('ALLOWED_HOST').replace(' ','').split(',')
CORS_ALLOWED_ORIGINS = env('ALLOWED_ORIGIN').replace(' ','').split(',')
CSRF_TRUSTED_ORIGINS = env('TRUSTED_ORIGIN').replace(' ','').split(',')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.environ.get('MYSQL_DATABASE', 'mysql-db'),
        'USER': os.environ.get('MYSQL_USER', 'mysql-user'),
        'PASSWORD': os.environ.get('MYSQL_PASSWORD', 'mysql-password'),
        'HOST': os.environ.get('MYSQL_DATABASE_HOST', 'db'),
        'PORT': os.environ.get('MYSQL_DATABASE_PORT', 3306),
    }
}


STATIC_URL = env('STATIC_URL')
STATIC_ROOT = env('STATIC_ROOT')
MEDIA_URL=env('MEDIA_URL')
MEDIA_ROOT=env('MEDIA_ROOT')