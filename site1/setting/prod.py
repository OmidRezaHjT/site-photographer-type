from site1.settings import *



LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'file': {
            'level': 'ERROR',
            'class': 'logging.FileHandler',
            'filename': '/home/camoshan/public_html/django_errors.log',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['file'],
            'level': 'ERROR',
            'propagate': True,
        },
    },
}

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-fs(ye&^=shh#9&kqs-&rfzecu4s7=ydto0i&(ssqwm3jd941=f'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['www.camoshan.ir','camoshan.ir']

#INSTALLED_APPS = []


# sites framework
SITE_ID = 2



DATABASES = {
    'default': {
    'ENGINE': 'django.db.backends.mysql',
    'NAME': 'camoshan_camoshan',
    'USER': 'camoshan_omid',
    'PASSWORD': 'omid1385REZA',
    'HOST': 'localhost',
    'PORT': '3306',
    }
}


STATIC_URL = '/static/'
STATIC_ROOT = '/home/camoshan/public_html/static'
MEDIA_ROOT = '/home/camoshan/public_html/media'
STATICFILES_DIRS = [
    BASE_DIR / "statics",
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

## X-XSS-Protection
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
## Strict-Transport-Security
SECURE_HSTS_SECONDS = 15768000
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True
## that requests over HTTP are redirected to HTTPS. aslo can config in webserver
SECURE_SSL_REDIRECT = True 
X_FRAME_OPTIONS = 'SAMEORIGIN'
# for more security
CSRF_COOKIE_SECURE = True
CSRF_USE_SESSIONS = True
CSRF_COOKIE_HTTPONLY = True
SESSION_COOKIE_SECURE = True
SESSION_COOKIE_SAMESITE = 'Strict'