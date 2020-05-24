from django.utils.translation import gettext_lazy as _

from violation.behaviours.violation import BaseViolationModelMixin as ViolationModelMixin


class Violation(ViolationModelMixin):
    class Meta:
        app_label = 'violation'
        verbose_name = _('Violation')
        verbose_name_plural = _('Violations')
