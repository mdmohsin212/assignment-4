from django.shortcuts import render
from category.forms import *

# Create your views here.

def all_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
    form = CategoryForm()
    return render(request, 'category.html', {'form' : form})