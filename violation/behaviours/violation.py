from django.contrib.auth import get_user_model
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.utils.translation import gettext_lazy as _

User = get_user_model()


class BaseViolationModelMixin(models.Model):

    VIOLATION_STATUS_PENDING = 0 # whether violation is awaiting approval from admin
    VIOLATION_STATUS_ACCEPTED = 1 # whether violation has been accepted by admin
    VIOLATION_STATUS_REJECTED = 2 # whether violation was rejected by admin

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
    violator = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        related_name='violations_broken',
        null=True,
        blank=True
    )
    status = models.PositiveSmallIntegerField(
        choices=VIOLATION_STATUS_CHOICES,
        default=VIOLATION_STATUS_PENDING
    )
    is_violated = models.BooleanField(null=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        from violation.signals import report_handler
        super().save(*args, **kwargs)
        report_handler.send(
            sender=self.__class__,
            violation=self,
            violator=self.content_object
        )

    def __str__(self):
        return f'{self.reported_by} just reported {self.content_object} for violation'

    class Meta:
        abstract = True
        constraints = [
            models.UniqueConstraint(
                fields=['content_type', 'object_id', 'reported_by'],
                name='unique_violation_constraint'
            )
        ]


class ViolationRuleModelMixin(BaseViolationModelMixin):
    rules = models.ManyToManyField('violation.Rule', related_name='violations')

    class Meta:
        abstract = True
