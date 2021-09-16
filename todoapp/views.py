from todoapp.Form import CategoryForm, TaskForm
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

def create_task(request, id):
    current_category = get_object_or_404(Category, id=id)
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.created_at = timezone.now()
            task.category_id = current_category
            task.save()
            return redirect('tasks.index', id=current_category.id)
    else:
        form = TaskForm()
    return render(request, 'todoapp/create_task.html', {'form': form}, {'id': current_category.id})