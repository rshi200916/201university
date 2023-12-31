"""
Django settings for web project.

Generated by 'django-admin startproject' using Django 2.2.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os, sys


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
from django.conf import global_settings

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print(BASE_DIR)
#添加导包路径

sys.path.insert(0, os.path.join(BASE_DIR, 'apps'))
sys.path.insert(1, os.path.join(BASE_DIR, 'utils'))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '40-is!mcsg%*2ci09*=qott()k-p*&jc_ph6(0kpexc5wsp47h'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_mysql',
    'userapp',
    'homeapp',
    'verifications',
    'shop',
    'payment',
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

ROOT_URLCONF = 'web.urls'

TEMPLATES = [
{
        'BACKEND': 'django.template.backends.jinja2.Jinja2',
        'DIRS': [os.path.join(BASE_DIR, 'template')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
            'environment': 'web.utils.jinja2_env.environment'
        },
    },
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'web.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'website',
        'USER': 'website',
        'PASSWORD': '123456',
        'HOST': '127.0.0.1',
        'PORT': '3306',
    },
    # 'default': {
    #     'ENGINE': 'django.db.backends.mysql',
    #     'NAME': 'goods',
    #     'USER': 'linux',
    #     'PASSWORD': 'shiranran123',
    #     'HOST': '192.168.161.139',
    #     'PORT': '3306',
    #
    # },
    # 'shop_slave1': {
    #     'ENGINE': 'django.db.backends.mysql',
    #     'NAME': 'goods',
    #     'USER': 'linux',
    #     'PASSWORD': 'shiranran123',
    #     'HOST': '192.168.161.137',
    #     'PORT': '3306',
    # },
    # 'shop_slave2': {
    #     'ENGINE': 'django.db.backends.mysql',
    #     'NAME': 'goods',
    #     'USER': 'linux',
    #     'PASSWORD': 'shiranran123',
    #     'HOST': '192.168.161.138',
    #     'PORT': '3306',
# }

}

# DATABASE_ROUTERS = ['db_router.MysqlRouter']

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

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/


STATIC_URL = '/static/'

global_settings

#自定义认证模块
AUTHENTICATION_BACKENDS = ['userapp.auth.MultiAccountLogin']

#添加自定义用户认证模型类， 格式：应用名.模型类名

AUTH_USER_MODEL = 'userapp.Users'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')
]

#日志文件

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(lineno)d %(message)s'
        },
        'simple': {
            'format': '%(levelname)s %(module)s %(lineno)d %(message)s'
        },
    },
    'filters': {
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
    },
    'handlers': {
        'console': {
            'level': 'INFO',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        },
        'file': {
           'level': 'INFO',
           'class': 'logging.handlers.RotatingFileHandler',
           'filename': os.path.join(BASE_DIR, 'logging/login.log'),
           'maxBytes': 300*1024*1024,
           'backupCount': 10,
           'formatter': 'verbose',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console', 'file'],
            'propagate': True,
            'level': 'INFO',
        },

    }
}


#redis缓存,没有shop商品的缓存
CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://127.0.0.1:6379/0",
        "OPTIONS": {
            "CLIENT_CLASS":"django_redis.client.DefaultClient",

        }

    },
    "session": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://127.0.0.1:6379/1",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",

        }

    },
    "verify_code": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://127.0.0.1:6379/2",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",

        }

    },
    "result": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://127.0.0.1:6379/3",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",


        }
    },



}
SESSION_ENGINE = "django.contrib.sessions.backends.cache"
SESSION_CACHE_ALIAS = "session"

# fast_dfs setting
DEFAULT_FILE_STORAGE = 'utils.fastdfs.fdfs_storage.FastDFSStorage'


FDFS_URL = "http://192.168.161.144:80/"

# FDFS_CLIENT_CONF = os.path.join(BASE_DIR, '/utils/fastdfs/client.conf')
FDFS_CLIENT_CONF = "D:\\马氏兵\\Git\work\\201university\\website\\Scripts\\web\\web\\utils\\fastdfs\\client.conf"





#alipay setting
# LOGIN_URL = '/Login/'
APP_PRIVATE_KEY_STRING = open(os.path.join(BASE_DIR, 'apps/payment/keys/app_pay_private_key.pem')).read()
# print(APP_PRIVATE_KEY_STRING)
# 支付宝公钥
ALIPAY_PUBLIC_KEY_STRING = open(os.path.join(BASE_DIR, 'apps/payment/keys/alipay_public_key.pem')).read()

# 应用ID
# APP_ID = '21811100020676C8'
# APP_ID = 'SANDBOX_5Y927N2Z87C005085'
APP_ID = '9021000126631212'

# 加密方式
SIGN = 'RSA2'

# 是否是支付宝测试环境(沙箱环境)，如果采用真是支付宝环境，配置False
DEBUG = True

# 支付网关
ALIPAY_URL = 'https://openapi-sandbox.dl.alipaydev.com/gateway.do'
# ALIPAY_URL = 'https://openapi.alipaydev.com/gateway.do'
# ALIPAY_URL = 'https://mapi.alipay.com/gateway.do'
ALIPAY_RETURN_URL = 'https:127.0.0.1:8000/shop/payment'


