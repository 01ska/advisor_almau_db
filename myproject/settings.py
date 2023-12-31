"""
Django settings for myproject project.

Generated by 'django-admin startproject' using Django 4.2.2.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-%c@%3%%(so@4i8+4h(3-&c)=5ik$tvl%gb%at1zinq97ux3k17'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'page',
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

ROOT_URLCONF = 'myproject.urls'

TEMPLATES = [
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

WSGI_APPLICATION = 'myproject.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME':'almau',
        'USER': 'root',
        'PASSWORD': '87015516777Tik@',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}



# import asyncio
# import aiomysql
#
# async def connect_to_database():
#     try:
#         # Параметры подключения к базе данных MySQL
#         db_config = {
#             'host': '192.168.45.217',
#             'port': 3306,
#             'user': 'student',
#             'password': 'pxZB9EFv',
#             'db': 'almauadvisor',
#         }
#
#         # Создание асинхронного подключения к базе данных
#         conn = await aiomysql.connect(**db_config)
#
#         # Получение курсора для выполнения SQL-запросов
#         cursor = await conn.cursor()
#
#         # Пример выполнения SQL-запроса
#         await cursor.execute('SELECT * FROM bachelor')
#
#         # Получение результатов запроса
#         results = await cursor.fetchall()
#         print(results)
#
#         # Закрытие курсора и соединения
#         await cursor.close()
#         conn.close()
#
#     except Exception as e:
#         print(f'Произошла ошибка при подключении: {e}')
#
# # Запуск асинхронной функции
# loop = asyncio.get_event_loop()
# loop.run_until_complete(connect_to_database())
# loop.close()
#
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': 'almauadvisor',
#         'USER': 'almaustud',
#         'PASSWORD': 'NCn6VTxW',
#         'HOST': '127.0.0.1',
#         'PORT': '3307',  # Используем порт локального подключения через SSH-туннель
#     }
# }

# from django.db import connections
# from django.db.utils import OperationalError
#
# def check_database_connection():
#     default_db_connection = connections['default']
#     try:
#         # Выполняем тестовый запрос к базе данных для проверки подключения
#         default_db_connection.cursor().execute("SELECT 1")
#         print("Подключение к базе данных активно и работает.")
#     except OperationalError as e:
#         print("Ошибка подключения к базе данных:", e)
#
#
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME':'almauadvisor',
#         'USER': 'almaustud',
#         'PASSWORD': 'NCn6VTxW',
#         'HOST': '127.0.0.1',
#         'PORT': '3306',
#     }
# }


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
