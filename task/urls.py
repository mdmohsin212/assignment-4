from django.urls import path
from task.views import *

urlpatterns = [
    path('task/', all_task, name='task'),
    path('edit/<int:id>', task_edit, name='edit'),
    path('delete/<int:id>', task_delete, name='delete'),
]