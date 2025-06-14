import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-p1oe3x2mtd_5^@4a29q)(+5d-8uj)oii)t+v0m%y@l71s2!(xz'

DEBUG = False

if not DEBUG:
    STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
    WHITENOISE_MANIFEST_STRICT = False

ALLOWED_HOSTS = ['crefito2.qvsaude.com.br' , '.vercel.app', 'localhost', ]

INSTALLED_APPS = [
    'jazzmin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'AESP_odonto',
    'empresas_AESP_odonto'
]

JAZZMIN_SETTINGS = {
    "site_title": "Qv Admin",
    "site_header": "Qv Admin",
    "site_brand": "Qv Admin",
    
    
    # Links to put along the top menu
    "topmenu_links": [

        # Url that gets reversed (Permissions can be added)
        {"name": "Home",  "url": "admin:index", "permissions": ["auth.view_user"]},

        # external url that opens in a new window (Permissions can be added)
        {"name": "listar Beneficiarios", "url": "/list/", "new_window": False},
    ],

    # Whether to show the UI customizer on the sidebar
    "show_ui_builder": False,
}

JAZZMIN_UI_TWEAKS = {
    "theme": "superhero",
    "dark_mode_theme": "cyborg",
}

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

# Configuração adicional para WhiteNoise
WHITENOISE_ROOT = os.path.join(BASE_DIR, 'staticfiles', 'root')

ROOT_URLCONF = 'core.urls'

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

WSGI_APPLICATION = 'core.wsgi.app'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('PGDATABASE', 'neondb'),
        'USER': os.getenv('PGUSER', 'neondb_owner'),
        'PASSWORD': os.getenv('PGPASSWORD', 'npg_Oh2JiDGzZ3le'),
        'HOST': os.getenv('PGHOST', 'ep-dawn-mouse-a4rtipuj-pooler.us-east-1.aws.neon.tech'),
        'PORT': '5432',
        'OPTIONS': {
            'sslmode': 'require',  # Neon requer SSL
        },
    }
}

DATABASES['default']['CONN_MAX_AGE'] = 300  # Mantém conexões por 5 minutos
DATABASES['default']['CONN_HEALTH_CHECKS'] = True

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

USE_I18N = True

USE_TZ = True

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]  

STATICFILES_STORAGE = 'whitenoise.storage.CompressedStaticFilesStorage'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


LANGUAGE_CODE = 'pt-br'
TIME_ZONE = 'America/Sao_Paulo'
CELERY_TIMEZONE = 'America/Sao_Paulo'


CELERY_BROKER_URL = 'redis://default:RSJQm2zvWJ93OnXzZDivnbR3s7oe3bMf@redis-15570.c308.sa-east-1-1.ec2.redns.redis-cloud.com:15570/0'
CELERY_RESULT_BACKEND = 'redis://default:RSJQm2zvWJ93OnXzZDivnbR3s7oe3bMf@redis-15570.c308.sa-east-1-1.ec2.redns.redis-cloud.com:15570/0'


EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.office365.com'  # Servidor SMTP do Outlook
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'cemaderj.aesp@brisecorretora.com.br'  # Seu endereço de email
EMAIL_HOST_PASSWORD = 'K)388560362189ah'  # Sua senha de email
DEFAULT_FROM_EMAIL = 'cemaderj.aesp@brisecorretora.com.br'