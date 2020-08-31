from django.db import models


class RuleManager(models.Manager):
    def rules_in(self, category):
        return self.filter(category__iexact=category)
