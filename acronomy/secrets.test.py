# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'just-a-testkey'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
Production = False

ADS_AUTH_TOKEN = None
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
    }
}

MEDIA_ROOT = 'testmediaroot'


MATOMO_API_KEY = None
