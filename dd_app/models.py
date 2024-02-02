from django.contrib.auth.models import User  # Userモデルをインポート
from django.db import models

# Create your models here.


class Video(models.Model):
    """動画を管理するためのORM
    """
    # 動画をアップロードしたユーザーを管理するためのフィールド
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # 動画のタイトルを管理するためのフィールド
    title = models.CharField(max_length=100)
    # 動画の説明を管理するためのフィールド
    description = models.TextField()
    # 動画ファイルをアップロードするためのフィールド
    video_file = models.FileField(upload_to='videos/')
    # いつ動画がアップロードされたかを管理するためのフィールド
    uploaded_at = models.DateTimeField(auto_now_add=True)
    # 動画が再生された回数をカウントするためのフィールド
    views = models.PositiveIntegerField(default=0)


class Comment(models.Model):
    """動画に対するコメントを管理するためのORM
    """
    # コメントがどの動画に対するものかを管理するためのフィールド
    video = models.ForeignKey(
        Video, on_delete=models.CASCADE, related_name='comments')
    # コメントの投稿者を管理するためのフィールド
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # コメントの本文を管理するためのフィールド
    text = models.TextField()
    # コメントが投稿された日時を管理するためのフィールド
    created_date = models.DateTimeField(auto_now_add=True)
