"""
Configurações do projeto HES Atacado.
Sistema de catálogo de produtos — Django + Supabase (PostgreSQL).
"""
from pathlib import Path
from decouple import config

# Caminho base do projeto
BASE_DIR = Path(__file__).resolve().parent.parent

# Pasta frontend (um nível acima do backend) — onde ficam html, css, js e img
FRONTEND_DIR = BASE_DIR.parent / 'frontend'

# ============================================
# SEGURANÇA / AMBIENTE
# ============================================
SECRET_KEY = config('SECRET_KEY')

# Em produção, defina DEBUG=False nas variáveis de ambiente do servidor
DEBUG = config('DEBUG', default=True, cast=bool)

# Hosts permitidos — vem do .env separado por vírgula
# Local: localhost,127.0.0.1   |   Produção: seu-app.koyeb.app,seudominio.com
_hosts = config('ALLOWED_HOSTS', default='localhost,127.0.0.1')
ALLOWED_HOSTS = [h.strip() for h in _hosts.split(',') if h.strip()]

# Origens confiáveis para CSRF (necessário para o login do /admin/ em HTTPS)
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
    'produtos',
]

# ============================================
# MIDDLEWARES
# WhiteNoise logo após o SecurityMiddleware serve os arquivos estáticos
# ============================================
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

ROOT_URLCONF = 'config.urls'

# Templates — lê direto da pasta frontend/html
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
        'CONN_MAX_AGE': 600,   # reaproveita conexões (importante em produção)
    }
}

# Validação de senhas
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

# ============================================
# INTERNACIONALIZAÇÃO
# ============================================
LANGUAGE_CODE = 'pt-br'
TIME_ZONE = 'America/Sao_Paulo'
USE_I18N = True
USE_TZ = True

# ============================================
# ARQUIVOS ESTÁTICOS (CSS, JS, img do frontend)
# ============================================
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    FRONTEND_DIR,
]
STATIC_ROOT = BASE_DIR / 'staticfiles'

# ============================================
# ARQUIVOS DE MÍDIA (fotos enviadas pelo admin)
# ============================================
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# ============================================
# COMPRESSÃO/ENTREGA DOS ESTÁTICOS (WhiteNoise)
# Django 4.2+ / 5.x
# ============================================
STORAGES = {
    'default': {
        'BACKEND': 'django.core.files.storage.FileSystemStorage',
    },
    'staticfiles': {
        'BACKEND': 'whitenoise.storage.CompressedManifestStaticFilesStorage',
    },
}

# ============================================
# E-MAIL (console durante desenvolvimento)
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
# SESSÃO — login ativo por 30 dias
# ============================================
SESSION_EXPIRE_AT_BROWSER_CLOSE = False
SESSION_COOKIE_AGE = 60 * 60 * 24 * 30  # 30 dias
SESSION_SAVE_EVERY_REQUEST = True       # renova a sessão a cada atividade

# ============================================
# SEGURANÇA EXTRA — só quando DEBUG=False (produção)
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