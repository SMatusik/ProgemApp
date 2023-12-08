from django.urls import path
from . import views

urlpatterns = [
    # path("", views.home, name="home"),
    # path("home", views.home, name="home"),
    # path("test-messages/", views.test_messages, name="test_messages"),
    # path("login-myself/", views.login_myself, name="login_myself"),

    path("register/", views.register, name="register"),
    path("password_reset/", views.password_reset, name="password_reset"),
    path("login/", views.login_view, name="login"),
    path("logout/",  views.log_out, name="logout"),
]