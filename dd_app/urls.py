from django.urls import path
from dd_app.views import VideoCreateView, TopPageView

urlpatterns = [
    path("video_upload/", VideoCreateView.as_view(), name="video_uploading_test"),
    path("", TopPageView.as_view(), name="home"),
]
