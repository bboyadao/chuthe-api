from django.apps import AppConfig


class AliasConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'alias'

    def ready(self):
        import chuthe.checks  # noqa: F401
