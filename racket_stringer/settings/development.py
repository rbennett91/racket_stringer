from .base import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ["SECRET_KEY"]

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = os.environ["ALLOWED_HOSTS"].split(", ")

# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": "racket_stringer.sqlite3",
    },
}