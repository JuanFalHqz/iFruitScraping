from .base import *

from decouple import config, Csv

# De string a booleano
DEBUG = config("DEBUG", cast=bool)

SECRET_KEY = config("SECRET_KEY")

ALLOWED_HOSTS = config('ALLOWED_HOSTS', cast=Csv())
# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
STATIC_ROOT = BASE_DIR / 'staticfiles'
