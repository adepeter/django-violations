from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class ViolationConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'violation'
    verbose_name = _('Violation')

    def ready(self):
        from . import signals
