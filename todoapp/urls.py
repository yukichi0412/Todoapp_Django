from django.urls import path
from . import views
from .views import CategoryViewSet, TaskViewSet

from rest_framework import routers


urlpatterns = [
    path('<int:id>/tasks', views.index, name='tasks.index'),
    path('create', views.create_category, name='categories.create'),
    path('<int:id>/tasks/create', views.create_task, name='tasks.create'),
    path('<int:id>/tasks/<int:task_id>', views.edit_task, name='tasks.edit'),
]

router = routers.DefaultRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'tasks', TaskViewSet)