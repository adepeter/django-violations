from django.utils.translation import gettext_lazy as _

from violation.behaviours.violation import ViolationRuleModelMixin as ViolationModelMixin


class Violation(ViolationModelMixin):
    class Meta:
        app_label = 'violation'
        verbose_name = _('violation')
        verbose_name_plural = _('violations')
