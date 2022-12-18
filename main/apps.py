from django.apps import AppConfig
from django.db.models.signals import post_save

class MainConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'main'

    def ready(self) -> None:
        from .signals import logtime_created