"""
Django settings for setup project.

Generated by 'django-admin startproject' using Django 4.1.1.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

import environ, os
import braintree
from pathlib import Path
from django.utils.translation import gettext_lazy as _


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Take environment variables from .env file
env = environ.Env()
env.read_env(os.path.join(BASE_DIR.parent, '.env'))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env.bool('DEBUG', default=True)

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    # django-apps
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    # third-apps
    'crispy_forms',
    'crispy_bootstrap4',
    'rosetta',
    'parler',
    # 'localflavor', # apps utilizado apenas como exemplo da funcionalidade
    # my-apps
    "apps.ecommerce",
    "apps.cart",
    "apps.orders",
    "apps.payment",
    "apps.coupons",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.locale.LocaleMiddleware", # add o pacote de traduções do Django
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "setup.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, 'templates')],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "apps.cart.context_processors.cart"
            ],
        },
    },
]

WSGI_APPLICATION = "setup.wsgi.application"


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

REDIS_HOST = 'localhost'
REDIS_PORT = 6379
REDIS_DB = 1
REDIS_PASSWORD = env('REDIS_DEFAULT_PASS', default="")


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = "en"

LANGUAGES = (
    ('en', _('English')),
    ('pt-br', _('Portuguese')),
)

TIME_ZONE = "America/Sao_Paulo"

USE_I18N = True

USE_TZ = True

LOCALE_PATH = os.path.join(BASE_DIR, 'locale/')

PARLER_LANGUAGES = {
    None: (
        {'code': 'en'},
        {'code': 'pt-br'},
    ),
    'default': {
        'fallback': 'pt-br',
        'hide_unstranslated': False,
    }
}


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

DATA_DIR = BASE_DIR.parent / 'data' / 'web'

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(DATA_DIR, 'static')
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]

MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media/")

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

CART_SESSION_ID = 'cart'

# crispy form
CRISPY_TEMPLATE_PACK = 'bootstrap4'

# EMAIL SMTP CONSOLE
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# Configurações para o Braintree
BRAINTREE_MERCHANT_ID = env('BRAINTREE_MERCHANT_ID', default="")
BRAINTREE_PUBLIC_KEY = env('BRAINTREE_PUBLIC_KEY', default="")
BRAINTREE_PRIVATE_KEY = env('BRAINTREE_PRIVATE_KEY', default="")

BRAINTREE_CONF = braintree.Configuration(
    braintree.Environment.Sandbox,
    BRAINTREE_MERCHANT_ID,
    BRAINTREE_PUBLIC_KEY,
    BRAINTREE_PRIVATE_KEY,
)

# CELERY
CELERY_TASK_ALWAYS_EAGER = True  # todas as tarefas serão executadas de forma síncrona (imediatamente) sem broker
CELERY_TASK_EAGER_PROPAGATES = True  # retorna o erro imeditamente ao chamador