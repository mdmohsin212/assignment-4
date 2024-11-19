from django.shortcuts import render, redirect
from task.forms import TaskForm
from task.models import TaskModel

# Create your views here.
def all_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    form = TaskForm()
    return render(request, 'task.html', {'form' : form})

def task_edit(request, id):
    task = TaskModel.objects.get(pk=id)
    task_form = TaskForm(instance=task)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('home')
    return render(request, 'task.html', {'form' : task_form})

def task_delete(request, id):
    TaskModel.objects.get(pk=id).delete()
    return redirect('home')