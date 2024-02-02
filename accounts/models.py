from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from dd_app.models import Video


class UserProfile(models.Model):
    # ユーザー情報を保存するフィールド
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # いいねした動画を保存するフィールド
    liked_video = models.ManyToManyField(Video, blank=True)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    """ユーザーが作成されたときに、UserProfileも作成する設定
    """
    if created:
        UserProfile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    """ユーザーが保存されたときに、UserProfileも保存する設定

    Args:
        sender (_type_): _description_
        instance (_type_): _description_
    """
    instance.userprofile.save()
