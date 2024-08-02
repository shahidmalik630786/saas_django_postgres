from django.contrib import admin
from django.urls import path, include
from . import views
from custom_auth import views as auth_view
from profiles import views as pro_view

urlpatterns = [
    path('username/<str:username>/', pro_view.profile_detail_view, name='profile_detail_view'),
    path('profile_list_view/', pro_view.profile_list_view, name='profile_list_view'),
]