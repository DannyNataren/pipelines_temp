from pathlib import Path

from pipelines_backend.settings.base import *

BASE_DIR = Path(__file__).resolve().parent.parent

DEBUG = True

ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'pipelines',
        'USER': 'postgres',
        'PASSWORD': 'Nintendo64',
        'HOST': 'localhost',
        'PORT': '5432'
    }
}

STATIC_URL = 'static/'

