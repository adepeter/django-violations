from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _

User = get_user_model()


class BaseRuleModelMixin(models.Model):
    CATEGORY_USER = 'user'
    CATEGORY_FORUM = 'forum'
    CATEGORY_POST = 'post'
    CATEGORY_THREAD = 'thread'
    CATEGORY_GENERAL = 'general'

    CATEGORY_CHOICES = [
        (CATEGORY_POST, _('Post')),
        (CATEGORY_FORUM, _('Forum')),
        (CATEGORY_THREAD, _('Thread')),
        (CATEGORY_USER, _('User')),
        (CATEGORY_GENERAL, _('General')),
    ]

    category = models.CharField(
        verbose_name=_('category'),
        max_length=10,
        choices=CATEGORY_CHOICES,
        blank=True,
        null=True
    )
    name = models.CharField(verbose_name=_('name'), max_length=255)
    description = models.TextField(verbose_name=_('description'))
    added_by = models.ForeignKey(
        User,
        verbose_name=_('Added by'),
        on_delete=models.DO_NOTHING,
        related_name='+',
        null=True,
        blank=True
    )

    def __str__(self):
        return f'{self.name} - {self.get_category_display()}'

    class Meta:
        abstract = True
        ordering = ['name']
