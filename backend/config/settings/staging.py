from .base import *



#
# Local Docker
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
