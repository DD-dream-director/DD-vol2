from django import forms
from django.core.exceptions import ValidationError
from dd_app.models import Video


class VideoForm(forms.ModelForm):
    """動画投稿用のフォームクラス"""

    class Meta:
        model = Video  # 使用するモデルを指定
        fields = [
            "title",
            "description",
            "video_file",
            "video_url",
            "tag",
        ]  # フォームで入力するフィールドを指定

    def clean(self):
        """動画ファイルと動画URLのどちらか一方が必要なことを確認するためのメソッド
        -> 不正な入力をサニタイジングする
        """
        cleaned_data = super().clean()
        video_file = cleaned_data.get("video_file")
        video_url = cleaned_data.get("video_url")
        if not video_file and not video_url:
            raise ValidationError("ファイルとURLのうちどちらか一つは必要です")
        return cleaned_data
