from django.contrib import admin
from django.urls import path, include
from Task_management.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('', include('task.urls')),
    path('', include('category.urls')),
]
