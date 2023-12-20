from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.forms import CharField, EmailField, PasswordInput, Textarea, TextInput
from user.models import CustomUser


class RegisterForm(UserCreationForm):
    email = EmailField()

    class Meta:
        model = CustomUser
        fields = ["email", "first_name", "last_name", "password1", "password2"]
        widgets = {
            "first_name": Textarea(attrs={"rows": 1, "cols": 15}),
            "last_name": Textarea(attrs={"rows": 1, "cols": 15}),
        }


class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)

    email = EmailField(
        widget=TextInput(
            attrs={"class": "form-control", "placeholder": "", "id": "hello"}
        )
    )
    password = CharField(
        widget=PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "password?",
                "id": "hi",
            }
        )
    )
