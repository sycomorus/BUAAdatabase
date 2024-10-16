from django.contrib import admin
from django.urls import path
from .views import login, register, get_routes_config, sendPost

urlpatterns = [
    path('login/', login, name='login'),
    path('register/', register, name='register'),
    path('sendPost/', sendPost, name='sendPost'),
    path('routes/', get_routes_config, name='get_routes_config'),
]