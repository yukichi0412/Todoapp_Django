from django import forms
from .models import Category

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