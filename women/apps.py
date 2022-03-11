from django.apps import AppConfig


class WomenConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'women'

    def ready(self):
        import women.signals  # noqa