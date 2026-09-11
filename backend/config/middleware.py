from django.contrib.auth import logout

class AdminSessionOnlyMiddleware:
    """
    Mantém o login do admin vivo apenas enquanto o usuário navega dentro de /admin/.
    Ao voltar para o site público, a sessão é encerrada — então o próximo
    acesso ao /admin/ vai pedir login de novo.
    """

    # Prefixos que NÃO devem derrubar a sessão
    IGNORAR = ('/admin/', '/static/', '/media/', '/api/')

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if (
            request.user.is_authenticated
            and request.user.is_staff
            and not request.path.startswith(self.IGNORAR)
        ):
            logout(request)
        return self.get_response(request)