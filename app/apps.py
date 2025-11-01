from django.apps import AppConfig

class MyAppConfig(AppConfig):  # Nome mais específico
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'app'
