import os
import django
from django.conf import settings


def load():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'hospital_project.settings')
    if not settings.configured:
        django.setup()