"""
Django settings for inq project.

Generated by 'django-admin startproject' using Django 4.0.2.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""

from pathlib import Path
import os
import stripe
import django_heroku
import dj_database_url

#from decouple import config

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

#STATIC_ROOT=BASE_DIR/'staticfiles'


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-ss@p#nm(uco180a3w%lz^2urbj(22o$r171k_++@*#msb$a$y7'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['127.0.0.1:8000','inqulino.herokuapp.com']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'inqu.apps.InquConfig',
    

    
    
    
    
]
SITE_ID = 1 

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'inq.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR,'template',],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'inq.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR /'db.sqlite3',
        


    }
}


# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = 'static/'

MEDIA_URL='/file/'
MEDIA_ROOT=os.path.join(BASE_DIR,'file')

if DEBUG:
    STATICFILES_DIRS=[(os.path.join(BASE_DIR,'static'),)]
else:
    STATIC_ROOT = os.path.join(BASE_DIR,'static')


STATICFILES_STORAGE='whitenoise.storage.CompressedStaticFilesStorage'


# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

razorpay_id='rzp_test_J6R52IMFm4mxzu'
razorpay_key='IZSGViOgt3GJ5Yde3NgKW7Po'

stripe.api_key = "price_1Kw2jsSH9T6h17WB05BxhCwK"


#https://buy.stripe.com/test_6oEcP80qa3iW8Kc3cc

#

django_heroku.settings(locals())

STRIPE_PUBLISHABLE_KEY = 'pk_test_51Kw2h5SH9T6h17WBpVYjECW0ipM2p3WLHA40dl1MXVXoff32EEu2CRTZt863GZTA1nL3XSGgAgq5aMq9NXJZmFVP00BYnNcYi6'
STRIPE_SECRET_KEY = 'sk_test_51Kw2h5SH9T6h17WBarOW5emJ6tcUHIFBK3u2vsx7Z7dqtf3QdEeuwHywsbUG8e4gLENJhh0NHo9siCuvoAZfgkjr00QLuAdt9T'