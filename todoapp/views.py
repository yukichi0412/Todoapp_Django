from todoapp.Form import CategoryForm
from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone
from .models import Category, Task

# Create your views here.
def index(request, id):
    categories = Category.objects.filter(created_at__lte=timezone.now()).order_by('created_at')
    current_category = get_object_or_404(Category, id=id)
    tasks = Task.objects.filter(category_id = current_category.id)
    
    return render(request, 'todoapp/index.html', 
        {'categories':categories, 'tasks':tasks, 'current_category_id':current_category.id})

def create_category(request):
    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            category = form.save(commit=False)
            category.created_at = timezone.now()
            category.save()
            return redirect('tasks.index', id=category.id)
    else:
        form = CategoryForm()
    return render(request, 'todoapp/create_category.html', {'form': form})
