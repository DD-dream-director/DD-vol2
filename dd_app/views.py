from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.


class HomeView(TemplateView):
    template_name = "home.html"


class LoginView(TemplateView):
    template_name = "login.html"


class RegisterUserView(TemplateView):
    template_name = "register_user.html"


class PostMovieView(TemplateView):
    template_name = "post_movie.html"


class SetupTagView(TemplateView):
    template_name = "setup_tag.html"


class ShowVideoDetailView(TemplateView):
    template_name = "show_video_detail.html"
