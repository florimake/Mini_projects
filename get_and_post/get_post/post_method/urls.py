from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('', post_view, name='post_method'),
]