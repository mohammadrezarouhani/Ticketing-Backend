"""
WSGI config for ticketing_backend project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/wsgi/
"""

from .profile import *

from django.core.wsgi import get_wsgi_application

application = get_wsgi_application()
