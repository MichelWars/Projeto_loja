from django.apps import AppConfig


class EntradasConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'entradas'
    
    def ready(self):
        import entradas.signals
