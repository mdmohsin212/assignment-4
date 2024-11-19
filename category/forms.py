from django import forms
from category.models import CategoryModel


class CategoryForm(forms.ModelForm):
    class Meta:
        model = CategoryModel
        fields = '__all__'
        
        labels = {
            'name' : 'Add Category',
        }