"""
WSGI config for Robu project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application


from decouple import config

# Load environment variable using config from decouple
environment = config('DJANGO_ENV', default='development')

# Set the Django settings module based on the environment
if environment == 'production':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Robu.settings.production')
else:
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Robu.settings.development')

application = get_wsgi_application()
