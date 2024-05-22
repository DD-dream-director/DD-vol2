from django.shortcuts import render
from django.contrib.auth.views import LoginView
from django.urls import reverse
from django.urls import reverse_lazy
from django.views import generic
from .forms import SignUpForm


# Create your views here.
class CustomLoginView(LoginView):
    template_name = "login.html"
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse("home")  # ログイン成功後のリダイレクト先


class SignUpView(generic.CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy("setup_tag")
    template_name = "register_user.html"
