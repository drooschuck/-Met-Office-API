from django.contrib import admin
from django.urls import path
from . import views
from .views import weather

urlpatterns = [
    path('',views.weather,name='weather')
    ]