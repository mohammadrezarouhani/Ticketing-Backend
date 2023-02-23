import os 

setting_module=os.environ.get('DJANGO_SETTINGS_MODULE')

if not setting_module:
    os.environ.setdefault('DJANGO_SETTINGS_MODULE','automation_core.settings.dev')
