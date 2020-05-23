from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Thread(models.Model):
    starter = models.ForeignKey(User, on_delete=models.CASCADE, related_name='threads')
    title = models.CharField(max_length=255)
    text = models.TextField()

    def __str__(self):
        return '%s by %s' % (self.title, self.starter.username)
