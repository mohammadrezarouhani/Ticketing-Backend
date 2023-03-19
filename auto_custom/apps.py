from django.apps import AppConfig


class AutoCustomConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'auto_custom'

    def ready(self) -> None:
        import auto_custom.signals
        return super().ready()
