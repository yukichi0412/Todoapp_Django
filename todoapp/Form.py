from django import forms
from .models import Category, Task

class CategoryForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(CategoryForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs = {
                'class': 'form-cotrol'
            }

    class Meta:
        model = Category
        fields = ('title',)
        labels = {'title': 'カテゴリ名'}

class TaskForm(forms.ModelForm):
    
    def __init__(self, *args, **kwargs):
        super(TaskForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs = {
                'class': 'form-control'
            }
    
    class Meta:
        STATUS_CHOICES = [(1, '未完了'), (2, '作業中'), (3, '完了')]

        model = Task
        fields = ('title', 'status', 'due_date')
        labels = {
            'title': 'タスク名',
            'status': 'ステータス',
            'due_date': '期限',
        }