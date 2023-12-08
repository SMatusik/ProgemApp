from typing import Dict, Any

from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect

from .forms import RegisterForm, LoginForm


def home(request):
    # just test view
    num_visits = request.session.get("num_visits", 0)
    request.session["num_visits"] = num_visits + 1
    context: Dict[str, Any] = {
        "count": request.session.get("num_visits", 1),
    }

    if request.user.is_authenticated:
        username = request.user.username
        context["username"] = username

    return render(request, "home.html", context=context)


def test_messages(request):
    # view to test some things
    messages.success(request=request, message="teeest")

    return render(request, "home.html")


def login_myself(request):
    # view to fast log-in
    user = authenticate(request, username="sebastian", password="progem")

    if user is not None:
        login(request, user)

    return render(request, "home.html")

def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "You've been registered mate" )
            return redirect("/home")
        messages.error(request, "Unsuccessful registration. Registration form is not valid.")
    form = RegisterForm()
    return render (request=request, template_name="registration/register.html", context={"register_form":form})


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

            messages.error(request, 'Invalid username or password')

    return render(request, 'registration/login.html')


def password_reset(request):
    pass


def log_out(request):
    logout(request)

    messages.success(request, "You've been logged out, mate.")
    return render(request, 'work_in_progress.html')
