from django.apps import AppConfig


class ViolationsConfig(AppConfig):
    name = 'apps.violations'

    def ready(self):
        from . import signals
