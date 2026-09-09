# =============================================
# Cria o superusuário padrão do admin automaticamente.
# Rode DEPOIS do migrate:  python criar_admin.py
# Se o usuário já existir, ele apenas avisa (não duplica).
# =============================================

import os
import django

# Configura o Django para rodar fora do manage.py
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from django.contrib.auth import get_user_model

User = get_user_model()

# Credenciais padrão do admin (definitivas para todos)
ADMIN_USER = 'hesadmin'
ADMIN_EMAIL = 'admin@hesatacado.com.br'
ADMIN_PASSWORD = 'hesadmin123'

if User.objects.filter(username=ADMIN_USER).exists():
    print(f'[OK] Superusuário "{ADMIN_USER}" já existe — nada a fazer.')
else:
    User.objects.create_superuser(
        username=ADMIN_USER,
        email=ADMIN_EMAIL,
        password=ADMIN_PASSWORD
    )
    print(f'[OK] Superusuário "{ADMIN_USER}" criado com sucesso!')
    print(f'     Login: {ADMIN_USER} / Senha: {ADMIN_PASSWORD}')