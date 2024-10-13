from django.contrib import admin
from django.urls import path
from .views import login, register, get_routes_config, home

urlpatterns = [
    path('', home, name='home'),  # 添加根路径 URL 配置
    path('login/', login, name='login'),
    path('register/', register, name='register'),
    path('routes/', get_routes_config, name='get_routes_config'),
]