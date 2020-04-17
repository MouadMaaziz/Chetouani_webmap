"""
Django settings for webmap project.

Generated by 'django-admin startproject' using Django 2.2.4.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os
import json

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '=_j#^9l4f6b^)-07)057&mcgs#tbbnyu^!p7f%52+#l426b_b$'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
#   '178.79.159.251','www.chetopgeo.com','chetopgeo.com'
ALLOWED_HOSTS = ['178.79.159.251','www.chetopgeo.com','chetopgeo.com']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'Map',
    'django.contrib.gis',
    'leaflet',
    'djgeojson',
    'Blog_app',
    'ckeditor',
    'ckeditor_uploader',



]


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'webmap.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
        'webmap/taroudant_etabs/templates'
        ],
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

WSGI_APPLICATION = 'webmap.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': 'mouad',
        'USER': 'postgres',
        'HOST': 'localhost',
        'PASSWORD':'mouadpass',
        'PORT':'5432',
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'fr'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
'''
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "webmap/static"),

]
'''
STATIC_ROOT= os.path.join(BASE_DIR,'webmap/static/') # add webmap/static/ for production

STATIC_URL = '/static/'

MEDIA_URL= '/media/'
MEDIA_ROOT= os.path.join(BASE_DIR,'media')

CKEDITOR_UPLOAD_PATH="media"

LEAFLET_CONFIG = {
    'DEFAULT_CENTER': (29,-8.86),
    'DEFAULT_ZOOM':4,
    'MIN_ZOOM':5,
    'SPATIAL_EXTENT':(0,18,-21,46),
    'ATTRIBUTION_PREFIX':'CTG',
    'TILES': [('Routes', 'https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', { }),
         ('Satellite','https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}', {'attribution': 'Tiles &copy;','maxZoom': 17}),
         ('Villes', 'http://stamen-tiles-{s}.a.ssl.fastly.net/toner/{z}/{x}/{y}.png', { }),
          ],
}



#GMAIL_CONF

EMAIL_BACKEND= 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_USE_TLS= True
EMAIL_PORT= 587
EMAIL_HOST_USER= 'mouad.maaziz@gmail.com'
EMAIL_HOST_PASSWORD= 'GreyForTheWin'
