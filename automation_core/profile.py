import os 
profile=os.environ.get('profile','dev')

if profile=='prod':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE','automation_core.settings.prod')
elif profile=='dev':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE','automation_core.settings.dev')
elif profile=='test':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE','automation_core.settings.test')