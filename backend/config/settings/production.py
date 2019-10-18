# settings/production.py

from .base import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

# TODO:: 設定する
# API サーバーだと*かも...
ALLOWED_HOSTS = ['yourcustomdomain.com', '.yourcustomdomain.com']



# Running locally so connect to either a local MySQL instance or connect to
# Cloud SQL via the proxy. To start the proxy via command line:
#
#     $ cloud_sql_proxy -instances=[INSTANCE_CONNECTION_NAME]=tcp:3306
#
# See https://cloud.google.com/sql/docs/mysql-connect-proxy

#
# production Databese
# [START db_setup]
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'HOST': 'db', # docker
        # 'HOST': '127.0.0.1',
        'PORT': '3306',
        'NAME': 'freespotbeauty',
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
