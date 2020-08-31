from django.db import models
from django.contrib.contenttypes.models import ContentType


class ViolationManager(models.Manager):
    def get_violations_for(self, obj, **kwargs):
        return self.filter(
            content_type=ContentType.objects.get_for_model(obj),
            object_id=obj.id,
            **kwargs
        )
