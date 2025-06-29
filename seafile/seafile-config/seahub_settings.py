# -*- coding: utf-8 -*-
# This is an example Seahub Settings configuration

# The environment file (.env) should handle these variables. 
SECRET_KEY = "YOUR_SECERET_KEY"
SERVICE_URL = "https://DOMAINNAME.COM" # The hostname you entered should be displayed

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'seahub_db',
        'USER': 'USERNAME',
        'PASSWORD': 'PASSWORD',
        'HOST': 'db',
        'PORT': '3306',
        'OPTIONS': {'charset': 'utf8mb4'},
    }
}

CACHES = {
    'default': {
        'BACKEND': 'django_pylibmc.memcached.PyLibMCCache',
        'LOCATION': 'memcached:11211',
    },
    'locmem': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
    },
}
COMPRESS_CACHE_BACKEND = 'locmem'

# The environment file should handle these variables. 
TIME_ZONE = 'Africa/Johannesburg' # The selected time zone should be displayed
FILE_SERVER_ROOT = 'https://DOMAINNAME.COM/seafhttp' # The hostname you entered should be displayed

# ****************The only change that should be applied is the addition of the line below*********************
CSRF_TRUSTED_ORIGINS = ['https://DOMAINNAME.COM'] # Replace DOMAINNAME.COM with your registered hostname (e.g app.seafile.com)
