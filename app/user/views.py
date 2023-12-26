from typing import Any, Dict

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render
from user.models import CustomUser

from .forms import LoginForm, RegisterForm
from common.messages import MessageText


def home(request):
    # just test view
    num_visits = request.session.get("num_visits", 0)
    request.session["num_visits"] = num_visits + 1
    context: Dict[str, Any] = {
        "count": request.session.get("num_visits", 1),
    }

    if request.user.is_authenticated:
        context["user_email"] = request.user.email

    return render(request, "home.html", context=context)


def test_messages(request):
    # view to test some things
    messages.success(request=request, message=MessageText.TEST)

    return render(request, "home.html")


def login_myself(request):
    # view to fast log-in
    user = authenticate(request, username="seb@progem.com", password="progem")

    if user is not None:
        login(request, user)

    return redirect("home")


def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password1"]
            password_confirm = form.cleaned_data["password2"]

            if (
                CustomUser.objects.filter(email=email).exists()
                or CustomUser.objects.filter(email=email).exists()
            ):
                messages.error(request=request, message=MessageText.REGISTER.USER_ALREADY_EXISTS)
            elif password != password_confirm:
                messages.error(request, "Passwords do not match.")
            else:
                user = form.save()
                login(request, user)
                messages.success(request=request, message=MessageText.REGISTER.SUCCESS)
                return redirect("/home")
        else:
            messages.error(
                request=request, message=MessageText.REGISTER.FAILURE
            )
    else:
        form = RegisterForm()
    return render(
        request=request,
        template_name="registration/register.html",
        context={"register_form": form},
    )


def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        username = request.POST.get("login")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, message=MessageText.LOGIN.SUCCESS)
            return redirect("home")
        else:
            messages.error(request=request, message=MessageText.LOGIN.FAILURE)

    return render(request, "registration/login.html")


def password_reset(request):
    # TO DO
    pass


def log_out(request):
    logout(request)
    messages.success(request=request, message=MessageText.LOGOUT.SUCCESS)
    return redirect("/home")

