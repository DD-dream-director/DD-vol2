from django.shortcuts import render
from django.contrib.auth.views import LoginView
from django.urls import reverse


# Create your views here.
class CustomLoginView(LoginView):
    template_name = "login.html"
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse("home")  # ログイン成功後のリダイレクト先
