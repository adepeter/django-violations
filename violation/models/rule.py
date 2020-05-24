from django.utils.translation import gettext_lazy as _

from violation.behaviours.rule import BaseRuleModelMixin as RuleModelMixin


class Rule(RuleModelMixin):
    class Meta:
        app_label = 'violation'
        verbose_name = _('Rule')
        verbose_name_plural = _('Rules')
