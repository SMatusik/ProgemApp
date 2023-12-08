"""
URL configuration for Progem project.

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
from user import views as user_views


urlpatterns = [
    path("admin/", admin.site.urls),
    # user defined
    path("", user_views.home, name="home"),
    path("home/", user_views.home, name="home"),
    # accounts
    path("accounts/", include("user.urls")),
    # test views
    path("test-messages/", user_views.test_messages, name="test_messages"),
    path("login-myself/", user_views.login_myself, name="login_myself"),
]
