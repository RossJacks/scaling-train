"""WSGI config for ross_rotisserie project."""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ross_rotisserie.settings")

application = get_wsgi_application()
