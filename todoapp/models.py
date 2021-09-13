from django.db import models
from django.conf import settings
from django.utils import timezone

class Category(models.Model):
    title = models.CharField(max_length=20)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title
