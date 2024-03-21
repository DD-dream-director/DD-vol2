from django.db.models.base import Model as Model
from django.db.models.query import QuerySet
from django.shortcuts import render
import re
from django.views.generic import View ,DetailView
from .models import Video
import re


class Rendering_View(View):
    def youtube_embed(self, request, *args, **kwargs):
        video_ids = []
        youtube_urls = Video.objects.all()
        for youtube_url in youtube_urls:
            video_id_match = re.search(r'(?:youtube\.com\/(?:[^\/\n\s]+\/\S+\/|(?:v|e(?:mbed)?)\/|\S*?[?&]v=)|youtu\.be\/)([a-zA-Z0-9_-]{11})', youtube_url.video_url)
            if video_id_match:
                video_ids.append(video_id_match.group(1))
            
        return render(request, 'youtube_embed.html', {'video_ids': video_ids})


#詳細画面
class DetaiVideoView(DetailView):
    template_name = 'dd_app/detail.html'
    model = Video

    def get_object(self, queryset=None):
        # ここで適切なオブジェクトを取得するロジックを実装します。
        return Video.objects.get(pk=self.kwargs['pk'])


    

    