from django.shortcuts import render
from django.utils import timezone
from .models import Category

# Create your views here.
def index(request, id):
    categories = Category.objects.filter(created_at__lte=timezone.now()).order_by('created_at')
    return render(request, 'todoapp/index.html', {'categories':categories})

