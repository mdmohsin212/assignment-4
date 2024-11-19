from django import forms
from task.models import TaskModel

class TaskForm(forms.ModelForm):
    class Meta:
        model = TaskModel
        fields = '__all__'
        
        labels = {
            'taskTitle' : 'Title',
            'taskDes' : 'Description',
            'is_complete' : 'Complete',
        }
        widgets = {
            'Assign_date' : forms.DateInput(attrs={'type' : 'date'}),
        }