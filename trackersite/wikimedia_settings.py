# -*- coding: utf-8 -*-
# Django project settings for Wikimedia Continous Integration
# THIS IS NOT AN EXAMPLE CONFIGURATION
# If you want to generate settings.py, use support/makesettings.py
from __future__ import absolute_import
import os

import common_settings as _common
for item in dir(_common):
    if item not in _common._IGNORE:
        locals()[item] = getattr(_common, item)


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'tracker',
        'USER': 'root',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
        'OPTIONS': {
            'unix_socket': '/tmp/mysqld/mysqld.sock'
        },
        'TEST': {
            'COLLATION': 'utf8_general_ci'
        }
    }
}

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'LOCATION': 'tracker-test-cache',
    }
}

SECRET_KEY = '42'
PRODUCTION = False
TRACKER_DOCS_ROOT = os.path.join(os.environ['DEPLOY_DIR'], 'docs')
SITE_ID = 1
ADMIN_MEDIA_PREFIX = '/static/admin/'
STATIC_URL = '/static/'
RECAPTCHA_PUBLIC_KEY = ''
RECAPTCHA_PRIVATE_KEY = ''
SENDFILE_BACKEND = 'sendfile.backends.development'
BASE_URL = 'https://example.com'
GOOGLE_ANALYTICS = None
MEDIAINFO_MEDIAWIKI_API = None
PRODUCTION_URL = "https://tracker.wikimedia.cz"
TRACKER_MANUAL_LINK = None
MEDIAINFO_MEDIAWIKI_TEMPLATE = None
MEDIAINFO_MEDIAWIKI_INFO_TEMPLATE = 'Information'
