from django.urls import path
from . import views

urlpatterns = [
    path('<int:id>/tasks', views.index, name='tasks.index'),
    path('create', views.create_category, name='categories.create'),
    path('<int:id>/tasks/create', views.create_task, name='tasks.create'),
]