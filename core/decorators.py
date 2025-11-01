# core/decorators.py
from functools import wraps
from django.shortcuts import redirect
from django.urls import reverse
from django.contrib.auth.decorators import user_passes_test

def group_required(groups):
    """
    Aceita lista de IDs ou nomes de grupos. Superuser sempre passa.
    Usa request.user (auth Django).
    """
    if isinstance(groups, (int, str)):
        groups = [groups]

    def check(u):
        if not getattr(u, "is_authenticated", False):
            return False
        if getattr(u, "is_superuser", False):
            return True
        ids = [g for g in groups if isinstance(g, int)]
        names = [g for g in groups if isinstance(g, str)]
        return (
            (ids and u.groups.filter(id__in=ids).exists()) or
            (names and u.groups.filter(name__in=names).exists())
        )

    return user_passes_test(check, login_url='login')

def lojista_login_required(view_func):
    """
    Aceita login do lojista baseado em SESSÃO (is_authenticated + empresa_id_sessao)
    e também funciona se o usuário Django estiver autenticado.
    """
    @wraps(view_func)
    def _wrapped(request, *args, **kwargs):
        logged = (
            request.session.get('is_authenticated') or
            getattr(request.user, 'is_authenticated', False)
        )
        if not logged:
            login_url = reverse('login')
            return redirect(f"{login_url}?next={request.get_full_path()}")

        # No lojista, a empresa em sessão é obrigatória
        if not request.session.get('empresa_id_sessao'):
            login_url = reverse('login')
            return redirect(f"{login_url}?next={request.get_full_path()}")

        return view_func(request, *args, **kwargs)
    return _wrapped
