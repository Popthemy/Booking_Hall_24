"""
Django settings for Book_hall project.

Generated by 'django-admin startproject' using Django 5.0.2.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""

from pathlib import Path
import os

import cloudinary
# import cloudinary_storage

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-@=tt4_$^!g2lz288$j_+!5ug87%nctd%+ff=pxi7hxtb-1y^+g'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS =    [ '0.0.0.0:5578' ,'localhost', '127.0.0.1', 'localhost:800'] 


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'building.apps.BuildingConfig',
    'booking.apps.BookingConfig',
    'about_us.apps.AboutUsConfig',
    'user.apps.UserConfig',
    'phonenumber_field',
    'cloudinary',
    'cloudinary_storage',


]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',

    'whitenoise.middleware.WhiteNoiseMiddleware', #for static files when Debug=False

    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

]

ROOT_URLCONF = 'Book_hall.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR/'templates',],
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

WSGI_APPLICATION = 'Book_hall.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

# for postgres offline
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': 'Book_hall',
#         'USER': 'postgres',
#         'PASSWORD': 'leebackendengine',
#         'HOST': 'localhost',
#         'PORT': '5432',
#     }
# }

# railway postgres Db


DATABASES ={'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'railway',
        'USER': 'postgres',
        'PASSWORD': 'G4A5dfeebG1beec1*1egbFeF6A3bEFde',
        'HOST': 'roundhouse.proxy.rlwy.net',  # or the IP address of your PostgreSQL server
        'PORT': '54041',       # the default PostgreSQL port
    }
    }



# for sqlite
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/
# cloudinary details
# CLOUDINARY_STORAGE = {
#   'CLOUD_NAME': 'dtbf1jnph',
#   'API_KEY': '789776388615556',
#   'API_SECRET': 'L7Ln7dU37qWH0gt-O3E1wByvDVU',
# }

cloudinary.config(
    cloud_name="dtbf1jnph",
    api_key="789776388615556",
    api_secret="L7Ln7dU37qWH0gt-O3E1wByvDVU"
)

DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'
STATIC_URL = 'static/'
MEDIA_URL = ''

MEDIA_ROOT = BASE_DIR / 'static/images'
STATICFILES_DIRS = [BASE_DIR / 'static']
STATIC_ROOT = BASE_DIR / 'general_static'


# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Email
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 465
EMAIL_USE_SSL = True

EMAIL_HOST_USER = 'leebackgreen'
EMAIL_HOST_PASSWORD = 'mbkw nang droc pabt'
