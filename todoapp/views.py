from django.shortcuts import get_object_or_404, render
from django.utils import timezone
from .models import Category, Task

# Create your views here.
def index(request, id):
    categories = Category.objects.filter(created_at__lte=timezone.now()).order_by('created_at')
    current_category = get_object_or_404(Category, id=id)
    tasks = Task.objects.filter(category_id = current_category.id)
    
    return render(request, 'todoapp/index.html', 
        {'categories':categories, 'tasks':tasks, 'current_category_id':current_category.id})

