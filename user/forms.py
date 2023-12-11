from django.forms import EmailField, PasswordInput, TextInput, CharField
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField
from django.contrib.auth.models import User

from user.models import CustomUser


class RegisterForm(UserCreationForm):
    email = EmailField()

    class Meta:
        model = CustomUser
        fields = ["email", "first_name", "last_name", "password1", "password2"]


class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)

    email = EmailField(widget=TextInput(
        attrs={'class': 'form-control', 'placeholder': '', 'id': 'hello'}))
    password = CharField(widget=PasswordInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'password?',
            'id': 'hi',
        }
    ))