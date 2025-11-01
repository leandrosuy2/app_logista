from django.contrib.auth.backends import BaseBackend
from django.contrib.auth.hashers import check_password
from core.models import UserLojista
  # Importe do submódulo diretamente

class UserLojistaBackend(BaseBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = UserLojista.objects.get(email=username)
            if check_password(password, user.password):
                return user
        except UserLojista.DoesNotExist:
            return None
