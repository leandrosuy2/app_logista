from django.shortcuts import redirect

class EmpresaSessionMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Verifica se o usuário está autenticado e se `empresa_id` está definido
        if request.user.is_authenticated and 'empresa_id' not in request.session:
            return redirect('login')  # Redirecione ao login se `empresa_id` estiver ausente
        return self.get_response(request)
