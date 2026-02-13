"""ASGI config for ross_rotisserie project."""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ross_rotisserie.settings")

application = get_asgi_application()
