from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from .models import Video
from .forms import VideoForm

# Create your views here.


class VideoCreateView(CreateView):
    """動画をアップロードするためのビュー"""

    model = Video
    form_class = VideoForm
    template_name = "video_uploading_test.html"
    # success_url = reverse_lazy("video_list")  # 成功時のリダイレクト先

    def form_valid(self, form):
        """フォームのバリデーション処理を書く場所"""
        admin_user = get_object_or_404(User, username="admin")
        form.instance.uploaded_by = (
            admin_user  # ログインユーザーをadminユーザーに指定(テスト用)
        )
        return super().form_valid(form)
