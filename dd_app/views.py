from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.views.generic import TemplateView
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
    success_url = reverse_lazy("home")  # 成功時のリダイレクト先

    def form_valid(self, form):
        """フォームのバリデーション処理を書く場所"""
        admin_user = get_object_or_404(User, username="admin")
        form.instance.uploaded_by = (
            admin_user  # ログインユーザーをadminユーザーに指定(テスト用)
        )
        return super().form_valid(form)


class TopPageView(TemplateView):
    """トップページを表示するビュー"""

    template_name = "video_uploading_RedirectDestination_test.html"

    def get_context_data(self, **kwargs):
        """テンプレートに渡す変数を追加する"""
        context = super().get_context_data(**kwargs)
        context["video_list"] = Video.objects.all().order_by("-uploaded_at")[:5]
        return context
