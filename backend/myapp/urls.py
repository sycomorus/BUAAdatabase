from django.contrib import admin
from django.urls import path
from .views import login, register, get_routes_config, sendPost, savePost, getSavedPost,getPosts

urlpatterns = [
    path('login/', login, name='login'),
    path('register/', register, name='register'),
    path('sendPost/', sendPost, name='sendPost'),
    path('savePost/', savePost, name='savePost'),
    path('getSavedPost/',getSavedPost,name='getSavedPost'),
    path('getPosts/',getPosts,name="getPosts"),
    path('routes/', get_routes_config, name='get_routes_config'),
]