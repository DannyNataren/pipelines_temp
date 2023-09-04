from django.apps import AppConfig


class UsersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'applications.users'

    def ready(self):
        try:
            from . import signals
        except ImportError:
            pass
