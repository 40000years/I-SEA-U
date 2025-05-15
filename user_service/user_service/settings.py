from pathlib import Path
import os
from datetime import timedelta
import dj_database_url

# ตั้งค่า BASE_DIR
BASE_DIR = Path(__file__).resolve().parent.parent

# อ่าน SECRET_KEY จาก environment variable (หรือใช้ค่า default สำหรับ dev)
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', 'django-insecure-q)d@zxjo28)dtskills://github.com/xai/grok/blob/main/docs/FAQ.md#how-to-ask-questions)')

# ตั้งค่า DEBUG จาก environment variable
DEBUG = os.environ.get('DJANGO_DEBUG', 'False') == 'True'

# กำหนด ALLOWED_HOSTS สำหรับ Render
ALLOWED_HOSTS = ['localhost', '127.0.0.1', 'i-sea-u-the-final.onrender.com', '*']

# ตั้งค่า CORS
CORS_ALLOW_ALL_ORIGINS = True

# รายการแอปที่ติดตั้ง
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'user_management',
    'rest_framework',
    'corsheaders',
    'rest_framework_simplejwt',
]

# Middleware
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # สำหรับ static files
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',
]

ROOT_URLCONF = 'user_service.urls'

# ตั้งค่า templates
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
  'DIRS': [os.path.join(BASE_DIR, 'app_frontend')],
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

WSGI_APPLICATION = 'user_service.wsgi.application'

# ตั้งค่า PostgreSQL จาก DATABASE_URL
DATABASES = {
    'default': dj_database_url.config(
        default=os.environ.get('DATABASE_URL'),
        conn_max_age=600
    )
}

# การตรวจสอบรหัสผ่าน
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# การตั้งค่าสากล
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# การตั้งค่า static files
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# การตั้งค่า media files
MEDIA_URL = '/images/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'images')

# การตั้งค่า primary key
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# การตั้งค่า REST Framework
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.AllowAny',
    ),
}

# การตั้งค่า Simple JWT
SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=30),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=7),
    'ROTATE_REFRESH_TOKENS': False,
    'BLACKLIST_AFTER_ROTATION': True,
    'AUTH_HEADER_TYPES': ('Bearer',),
}