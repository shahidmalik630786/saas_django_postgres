"""
URL configuration for cfehome project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views
from custom_auth import views as auth_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home_view, name="home"),
    path('about', views.about_view),
    path("hello-world/", views.home_view),
    path("hello-world.html", views.home_view),
    path("login/", auth_view.login),
    path("register/", auth_view.register),
    path('accounts/', include('allauth.urls')),
    path("protected/", auth_view.pwd_protected),
    path("protected/user_only_view/", views.user_only_view),
    path("protected/staff_only_view/", views.staff_only_view),
    path("warning/staff/member/", views.staff_only_warning),
    path('profile/', include(('profiles.urls', 'profiles'), namespace='profile')),


]

