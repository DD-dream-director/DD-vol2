from django.db.models.base import Model as Model
from django.db.models.query import QuerySet
from django.shortcuts import render
import re
from django.views.generic import View ,DetailView
from .models import Video
import re


class Rendering_View(View):
    def get(self, request, *args, **kwargs):
        video_ids = []
        video_titles =[]
        video_pks = []
        videos = Video.objects.all()
        
        for video in videos:
            video_titles.append(video.title)
            video_pks.append(video.pk)
            video_id_match = re.search(r'(?:youtube\.com\/(?:[^\/\n\s]+\/\S+\/|(?:v|e(?:mbed)?)\/|\S*?[?&]v=)|youtu\.be\/)([a-zA-Z0-9_-]{11})', video.video_url)

            if video_id_match:
                video_ids.append(video_id_match.group(1))
            
            
        ziplist = zip(video_ids, video_titles,  video_pks)
                

        return render(request, 'youtube_embed.html', {'ziplist': ziplist})


#詳細画面
class DetailVideoView(DetailView):
    template_name = 'detail.html'
    model = Video
    context_object_name = "video"

    


    

    