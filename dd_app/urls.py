from django.urls import path, include
from .views import Rendering_View, DetailVideoView

urlpatterns = [
    path('', Rendering_View.as_view(), name='home'),
    path('detail/<int:pk>/', DetailVideoView.as_view(), name='detail')
]
