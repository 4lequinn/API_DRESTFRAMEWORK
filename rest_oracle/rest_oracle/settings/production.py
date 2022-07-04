from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.oracle',
        'NAME': '127.0.0.1:1521/orcl',
        'USER': 'p3liss',
        'PASSWORD' : 'p3liss',
        'TEST' : {
            'USER' : 'default_test_tbls',
            'TBLSPACE' : 'default_test_tbls',
            'TBLSPACE_TMP' : 'default_test_tbls_tmp'
        }
    }
}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = 'static/'

