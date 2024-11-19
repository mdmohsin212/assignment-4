from django.urls import path, include
from category.views import *

urlpatterns = [
    path('category/', all_category, name='category'),
]
