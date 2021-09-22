from rest_framework import serializers

from .models import Category, Task

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('title', 'created_at')

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('title', 'status', 'due_date', 'created_at', 'updated_at', 'category_id')
