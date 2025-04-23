from site1.settings import *

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-fs(ye&^=shh#9&kqs-&rfzecu4s7=ydto0i&(ssqwm3jd941=f'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['www.camoshan.ir','camoshan.ir']

#INSTALLED_APPS = []


# sites framework
SITE_ID = 1



DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
        }
    }


STATIC_ROOT = BASE_DIR / 'staticfiles'
MEDIA_ROOT = BASE_DIR / 'media'

STATICFILES_DIRS = [
    BASE_DIR / "static"
]



#CSRF_COOKIE_SECURE = True


# Forget pass
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'testforsite04@gmail.com'
EMAIL_HOST_PASSWORD = 'hwly hikp rkan cjbs'
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER