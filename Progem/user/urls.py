from django.urls import path
from . import views

urlpatterns = [
    path("register/", views.register, name="register"),
    path("login/", views.login_view, name="login"),
    path("logout/",  views.log_out, name="logout"),
    path("password_reset/", views.password_reset, name="password_reset"),
]