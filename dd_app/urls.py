from django.urls import path
from dd_app.views import *

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("login/", LoginView.as_view(), name="login"),
    path("register_user/", RegisterUserView.as_view(), name="register_user"),
    path("post_movie/", PostMovieView.as_view(), name="post_movie"),
    path("setup_tag/", SetupTagView.as_view(), name="setup_tag"),
    path("show_video_detail/", ShowVideoDetailView.as_view(), name="show_video_detail"),
]
