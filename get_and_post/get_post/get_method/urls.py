from django.contrib import admin
from django.urls import path
from .views import *


urlpatterns = [
    path('', get_view, name='get_method'),
]