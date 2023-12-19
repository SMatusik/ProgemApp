from typing import Dict, Any

from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.shortcuts import render, redirect

from .forms import RegisterForm, LoginForm
from user.models import CustomUser


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
    messages.success(request=request, message="teeest")

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
            email = form.cleaned_data['email']
            password = form.cleaned_data['password1']
            password_confirm = form.cleaned_data['password2']

            if CustomUser.objects.filter(email=email).exists() or CustomUser.objects.filter(email=email).exists():
                messages.error(request, "User with this username/email already exists.")
            elif password != password_confirm:
                messages.error(request, "Passwords do not match.")
            else:
                user = form.save()
                login(request, user)
                messages.success(request, "You've been registered mate")
                return redirect("/home")
        else:
            messages.error(request, "Unsuccessful registration. Registration form is not valid.")
    else:
        form = RegisterForm()
    return render(request=request, template_name="registration/register.html", context={"register_form": form})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        username = request.POST.get('login')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, message="You've been logged in!")
            return redirect('home')
        else:

            messages.error(request, 'Invalid email or password')

    return render(request, 'registration/login.html')


def password_reset(request):
    pass


def log_out(request):
    logout(request)

    messages.success(request, "You've been logged out, mate.")
    return redirect("/home")


def view_user_invitations(request):
    # Invitations
    return redirect("home")
