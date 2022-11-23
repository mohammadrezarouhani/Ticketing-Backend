from django.apps import AppConfig


class AutoConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'auto'
    
    def ready(self) -> None:
        import auto.signals
        return super().ready()