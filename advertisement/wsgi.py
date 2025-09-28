"""
WSGI config for advertisement project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

# Use production settings if RENDER environment variable is set
if os.environ.get('RENDER'):
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "advertisement.production_settings")
else:
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "advertisement.settings")

application = get_wsgi_application()
