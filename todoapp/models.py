from datetime import datetime
from django.db import models
from django.conf import settings
from django.utils import timezone

class Category(models.Model):
    title = models.CharField(max_length=20)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

class Task(models.Model):
    STATUS_CHOICES = [(1, '未完了'), (2, '作業中'), (3, '完了')]

    title = models.CharField(max_length=100)
    status = models.IntegerField(choices=STATUS_CHOICES, default=1)
    due_date = models.DateField(default=timezone.now)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)

    def publish(self):
        self.updated_at = timezone.now()
        self.save()

    def __str__(self):
        return self.title
