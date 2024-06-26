from django.contrib.auth.models import User
from django.db import models
from django.core.exceptions import ValidationError
from taggit.managers import TaggableManager

# Create your models here.


class Video(models.Model):
    """動画を管理するためのORM"""

    # 動画をアップロードしたユーザーを管理するためのフィールド
    uploaded_by = models.ForeignKey(User, on_delete=models.CASCADE)
    # 動画のタイトルを管理するためのフィールド
    title = models.CharField(max_length=100)
    # 動画のサムネイルをアップロードするためのフィールド
    thumbnail = models.ImageField(upload_to="thumbnails/", blank=True, null=False)
    # 動画の説明を管理するためのフィールド
    description = models.TextField()
    # 動画ファイルをアップロードするためのフィールド
    video_file = models.FileField(upload_to="videos/", blank=True, null=True)
    # 動画URLを管理するためのフィールド
    video_url = models.URLField(blank=True, null=True)
    # いつ動画がアップロードされたかを管理するためのフィールド
    uploaded_at = models.DateTimeField(auto_now_add=True)
    # 動画が再生された回数をカウントするためのフィールド
    view = models.PositiveIntegerField(default=0)
    # 動画がいいねされた回数をカウントするためのフィールド
    like = models.PositiveIntegerField(default=0)
    # タグを管理するためのフィールド
    tag = TaggableManager(blank=True)

    class Meta:
        # テーブル名をvideoに設定
        db_table = "video"

    def __str__(self):
        # 動画のタイトルを返す(管理画面で表示されるカラムの設定)
        return self.title

    def clean(self):
        """動画ファイルと動画URLのどちらか一方のみが必要なことを確認するためのメソッド"""
        if (self.video_file is None and self.video_url is None) or (
            self.video_file is not None and self.video_url is not None
        ):
            raise ValidationError("ファイルとURLのうちどちらか一つのみに値が必要です")


class Comment(models.Model):
    """動画に対するコメントを管理するためのORM"""

    # コメントがどの動画に対するものかを管理するためのフィールド
    video = models.ForeignKey(Video, on_delete=models.CASCADE, related_name="comments")
    # コメントの投稿者を管理するためのフィールド
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # コメントの本文を管理するためのフィールド
    text = models.TextField()
    # コメントが投稿された日時を管理するためのフィールド
    created_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        # テーブル名をcommentに設定
        db_table = "comment"

    def __str__(self):
        # コメントの本文を返す(管理画面で表示されるカラムの設定)
        return self.text
