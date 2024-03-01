from django.contrib import admin
from django.urls import path
from .views import blog

urlpatterns = [
    path('', blog, name= 'index' ),
]
