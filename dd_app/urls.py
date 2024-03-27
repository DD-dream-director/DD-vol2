from django.urls import path, include
from .views import Rendering_View

urlpatterns = [
    path('', Rendering_View.as_view(), name='home'),
]
