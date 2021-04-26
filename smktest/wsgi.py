"""
WSGI config for smktest project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'smktest.settings')

import django
django.setup()
from django.core.management import call_command

application = get_wsgi_application()

from logic.models import Players

players = Players.objects.count()

if players == 0:
    player_instance = Players.objects.create(name="Ana")
    player_instance.save()

    player_instance2 = Players.objects.create(name="Jose")
    player_instance2.save()

    player_instance3 = Players.objects.create(name="Juan")
    player_instance3.save()