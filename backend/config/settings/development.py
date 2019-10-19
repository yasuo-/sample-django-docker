# settings/development.py

from .base import *


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '=6z5^ty9$djg9!d&zbjc7sw0i^3=zlovqf9x!@(vh8&+mc-pdv'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['0.0.0.0']



#
# Local Docker
# [START db_setup]
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'HOST': 'db', # docker
        # 'HOST': '127.0.0.1',
        'PORT': '3306',
        'NAME': 'dbname',
        'USER': 'root',
        'PASSWORD': 'password',
    }
}
# [END db_setup]


# media files (upload image file)
MEDIA_ROOT = os.path.join(BASE_DIR, 'staticfiles', 'blob')
MEDIA_URL = '/blob/'


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles', 'static')
STATIC_URL = '/static/'
