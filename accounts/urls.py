from django.urls import path
from accounts import views

urlpatterns = [
    path("login/", views.CustomLoginView.as_view(), name="login"),
    path("signup/", views.SignUpView.as_view(), name="signup"),
]
