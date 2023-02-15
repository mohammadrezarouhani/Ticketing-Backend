from automation_core.settings.settings import *


env=environ.Env()
env.read_env(os.path.join(BASE_DIR,'environment','dev.env'))

SECRET_KEY = env('SECRET_KEY')
DEBUG = bool(int(env('DEBUG')))

ALLOWED_HOSTS = ['*']
CORS_ALLOW_ALL_ORIGINS=True
CSRF_TRUSTED_ORIGINS = ["http://localhost:8001","http://localhost:8001"]

REST_FRAMEWORK.update({'DEFAULT_SCHEMA_CLASS':'rest_framework.schemas.coreapi.AutoSchema' })

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

STATIC_URL = 'static/'
MEDIA_URL='/media/'
MEDIA_ROOT=os.path.join(BASE_DIR,'media')