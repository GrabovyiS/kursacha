import os
from pathlib import Path
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-luc0d%7a17@&d($z4*6#%jlnwrbp=&(wx2ps$u+y+itfqapg!1'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
BASE_DIR = Path(__file__).resolve().parent.parent
ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'std_1355_weather',
        'USER': 'std_1355_weather',
        'PASSWORD': 'testtest',
        'HOST': 'std-mysql.ist.mospolytech.ru',
        'PORT': '3306',
    }
}

STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_DIR = os.path.join(BASE_DIR, "static")
# STATICFILES_DIRS = (STATIC_DIR,)