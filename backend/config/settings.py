"""
Configurações do projeto HES Atacado.
Sistema de catálogo de produtos — Django + Supabase (PostgreSQL + Storage).
"""
from pathlib import Path
from decouple import config

# Caminho base do projeto
BASE_DIR = Path(__file__).resolve().parent.parent

# Pasta frontend (um nível acima do backend)
FRONTEND_DIR = BASE_DIR.parent / 'frontend'

# ============================================
# SEGURANÇA / AMBIENTE
# ============================================
SECRET_KEY = config('SECRET_KEY')
DEBUG = config('DEBUG', default=True, cast=bool)

_hosts = config('ALLOWED_HOSTS', default='localhost,127.0.0.1')
ALLOWED_HOSTS = [h.strip() for h in _hosts.split(',') if h.strip()]

_csrf = config('CSRF_TRUSTED_ORIGINS', default='')
CSRF_TRUSTED_ORIGINS = [o.strip() for o in _csrf.split(',') if o.strip()]

# ============================================
# APLICAÇÕES
# ============================================
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'storages',
    'produtos',
]

# AJUSTADO: evita aviso do Django e padroniza a PK
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# ============================================
# MIDDLEWARES
# ============================================
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'config.middleware.AdminSessionOnlyMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [FRONTEND_DIR / 'html'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'

# ============================================
# BANCO DE DADOS — Supabase (PostgreSQL)
# ============================================
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': config('DB_NAME'),
        'USER': config('DB_USER'),
        'PASSWORD': config('DB_PASSWORD'),
        'HOST': config('DB_HOST', default='localhost'),
        'PORT': config('DB_PORT', default='5432'),
        'CONN_MAX_AGE': 600,
        # AJUSTADO: testa a conexão antes de usar (importante com pooler)
        'CONN_HEALTH_CHECKS': True,
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# ============================================
# INTERNACIONALIZAÇÃO
# ============================================
LANGUAGE_CODE = 'pt-br'
TIME_ZONE = 'America/Sao_Paulo'
USE_I18N = True
USE_TZ = True

# ============================================
# ARQUIVOS ESTÁTICOS
# ============================================
STATIC_URL = '/static/'

# AJUSTADO: só inclui a pasta se ela existir de fato (evita quebrar o build)
STATICFILES_DIRS = [FRONTEND_DIR] if FRONTEND_DIR.exists() else []

STATIC_ROOT = BASE_DIR / 'staticfiles'

MEDIA_ROOT = BASE_DIR / 'media'

# ============================================
# SUPABASE STORAGE
# ============================================
SUPABASE_S3_ENDPOINT = config('SUPABASE_S3_ENDPOINT', default='')
SUPABASE_BUCKET = config('SUPABASE_BUCKET', default='produtos')
USE_SUPABASE_STORAGE = bool(SUPABASE_S3_ENDPOINT)

SUPABASE_PROJECT_REF = config('SUPABASE_PROJECT_REF', default='')
if not SUPABASE_PROJECT_REF and SUPABASE_S3_ENDPOINT:
    SUPABASE_PROJECT_REF = SUPABASE_S3_ENDPOINT.split('//')[-1].split('.')[0]

if USE_SUPABASE_STORAGE:
    AWS_ACCESS_KEY_ID = config('SUPABASE_S3_ACCESS_KEY')
    AWS_SECRET_ACCESS_KEY = config('SUPABASE_S3_SECRET_KEY')
    AWS_STORAGE_BUCKET_NAME = SUPABASE_BUCKET

    AWS_S3_ENDPOINT_URL = SUPABASE_S3_ENDPOINT
    AWS_S3_REGION_NAME = config('SUPABASE_S3_REGION', default='sa-east-1')
    AWS_S3_SIGNATURE_VERSION = 's3v4'
    AWS_S3_ADDRESSING_STYLE = 'path'
    AWS_S3_FILE_OVERWRITE = False

    # AJUSTADO: Supabase rejeita ACL em muitos casos -> gera erro no upload
    AWS_DEFAULT_ACL = None

    AWS_QUERYSTRING_AUTH = False

    AWS_S3_CUSTOM_DOMAIN = (
        f'{SUPABASE_PROJECT_REF}.supabase.co'
        f'/storage/v1/object/public/{SUPABASE_BUCKET}'
    )
    AWS_S3_URL_PROTOCOL = 'https:'
    MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/'
else:
    MEDIA_URL = '/media/'

# ============================================
# STORAGES
# ============================================
STORAGES = {
    'default': {
        'BACKEND': (
            'storages.backends.s3.S3Storage'
            if USE_SUPABASE_STORAGE
            else 'django.core.files.storage.FileSystemStorage'
        ),
    },
    'staticfiles': {
        # AJUSTADO: versão SEM manifest — serve o CSS direto, sem depender
        # do staticfiles.json. Elimina a maior causa de "site sem estilo".
        'BACKEND': 'whitenoise.storage.CompressedStaticFilesStorage',
    },
}

# ============================================
# E-MAIL
# ============================================
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# ============================================
# CACHE
# ============================================
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'LOCATION': 'cache-hes',
    }
}

# ============================================
# SESSÃO
# ============================================
SESSION_EXPIRE_AT_BROWSER_CLOSE = True
SESSION_COOKIE_AGE = 60 * 60 * 2
SESSION_SAVE_EVERY_REQUEST = False
SESSION_COOKIE_HTTPONLY = True

# ============================================
# SEGURANÇA EXTRA — produção
# ============================================
if not DEBUG:
    SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
    SECURE_SSL_REDIRECT = True
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True
    SECURE_HSTS_SECONDS = 31536000
    SECURE_HSTS_INCLUDE_SUBDOMAINS = True
    SECURE_HSTS_PRELOAD = True
    SECURE_CONTENT_TYPE_NOSNIFF = True