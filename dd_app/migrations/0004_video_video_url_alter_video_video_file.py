# Generated by Django 5.0.1 on 2024-02-04 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dd_app', '0003_video_tags'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='video_url',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='video',
            name='video_file',
            field=models.FileField(blank=True, null=True, upload_to='videos/'),
        ),
    ]
