# Generated by Django 5.0.1 on 2024-02-06 08:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dd_app', '0004_video_video_url_alter_video_video_file'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='icon',
            field=models.ImageField(blank=True, null=True, upload_to='icons/'),
        ),
    ]
