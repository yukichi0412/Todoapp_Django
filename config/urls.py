from todoapp import views
from django.contrib import admin
from django.urls import path, include
import sys
sys.path.append('../')
from todoapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('categories/', include('todoapp.urls')),
    path('', views.redirectview, name='anotherpage'),
]
