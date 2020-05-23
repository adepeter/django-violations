from django.contrib.auth import get_user_model
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.utils.translation import gettext_lazy as _

from .rule import Rule

User = get_user_model()


class Violation(models.Model):
    VIOLATION_STATUS_PENDING = 0
    VIOLATION_STATUS_ACCEPTED = 1
    VIOLATION_STATUS_REJECTED = 2

    VIOLATION_STATUS_CHOICES = (
        (VIOLATION_STATUS_PENDING, _('Pending')),
        (VIOLATION_STATUS_ACCEPTED, _('Accepted')),
        (VIOLATION_STATUS_REJECTED, _('Rejected')),
    )

    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    content_object = GenericForeignKey()
    object_id = models.PositiveIntegerField()

    reported_by = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        related_name='violations_reported',
        null=True
    )
    violated_by = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        related_name='violations_broken',
        null=True
    )
    rules = models.ManyToManyField(Rule, related_name='violations')
    status = models.PositiveSmallIntegerField(
        choices=VIOLATION_STATUS_CHOICES,
        default=VIOLATION_STATUS_PENDING
    )
    is_violated = models.NullBooleanField()

    def save(self, *args, **kwargs):
        from ..signals import report_handler
        super().save(*args, **kwargs)
        report_handler.send(
            sender=self.__class__,
            violation=self,
            violator=self.content_object
        )

    def __str__(self):
        return f'{self.reported_by} just reported {self.content_object} for violation'