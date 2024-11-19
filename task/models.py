from django.db import models
import datetime
from category.models import *
# Create your models here.

class TaskModel(models.Model):
    taskTitle = models.CharField(max_length=100)
    taskDes = models.TextField()
    category = models.ManyToManyField(CategoryModel)
    Assign_date = models.DateField(null=True, blank=True, default=datetime.date.today)
    is_complete = models.BooleanField(default=False)
    
    def __str__(self):
        return self.taskTitle