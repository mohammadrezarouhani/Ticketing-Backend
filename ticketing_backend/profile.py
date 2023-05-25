import os 
profile=os.environ.get('profile','dev')

if profile=='prod':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE','ticketing_backend.settings.prod')
elif profile=='dev':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE','ticketing_backend.settings.dev')
elif profile=='test':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE','ticketing_backend.settings.test')