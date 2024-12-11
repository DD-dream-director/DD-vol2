from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class SignUpForm(UserCreationForm):
    username = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "ユーザー名を入力"}
        ),
    )
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(
            attrs={"class": "form-control", "placeholder": "メールアドレスを入力"}
        ),
    )
    password1 = forms.CharField(
        required=True,
        widget=forms.PasswordInput(
            attrs={"class": "form-control", "placeholder": "パスワードを入力"}
        ),
    )
    password2 = forms.CharField(
        required=True,
        widget=forms.PasswordInput(
            attrs={"class": "form-control", "placeholder": "パスワードの再確認"}
        ),
    )

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")
        widgets = {
            "username": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "ユーザー名を入力"}
            ),
            "password1": forms.PasswordInput(
                attrs={"class": "form-control", "placeholder": "パスワードを入力"}
            ),
            "password2": forms.PasswordInput(
                attrs={"class": "form-control", "placeholder": "パスワードの再確認"}
            ),
        }
