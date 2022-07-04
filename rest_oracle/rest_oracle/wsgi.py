"""
WSGI config for rest_oracle project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

# Indicamos dónde estarán nuestros archivos de configuración
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'rest_oracle.settings.local.py')

application = get_wsgi_application()
