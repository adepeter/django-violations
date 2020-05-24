from django.apps import AppConfig


class ViolationsConfig(AppConfig):
    name = 'violations'

    def ready(self):
        from . import signals
