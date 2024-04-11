from django.db.models.base import Model as Model
from django.db.models.query import QuerySet
from django.shortcuts import render
import re
from django.views.generic import View ,DetailView
from .models import Video
import re
from moviepy.editor import VideoFileClip
from django.core.files.storage import default_storage



class Rendering_View(View):
    def get(self, request, *args, **kwargs):
        video_ids = []
        video_files = []
        video_titles =[]
        video_pks = []
        videos = Video.objects.all()
        
        for video in videos:
            video_titles.append(video.title)
            video_pks.append(video.pk)

            if video.video_file:
                # video_file = MOV_Conversion(video.video_file)
                
                video_ids.append(video.video_file)

            else:
                video_id_match = re.search(r'(?:youtube\.com\/(?:[^\/\n\s]+\/\S+\/|(?:v|e(?:mbed)?)\/|\S*?[?&]v=)|youtu\.be\/)([a-zA-Z0-9_-]{11})', video.video_url)
                video_ids.append(video_id_match.group(1)) 
            
        ziplist = zip(video_ids, video_titles,  video_pks)
                
        return render(request, 'youtube_embed.html', {'ziplist': ziplist})


#詳細画面
class DetailVideoView(DetailView):
    template_name = 'detail.html'
    model = Video

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        video = self.object
        youtube_video_id = self.get_youtube_video_id(video.video_url)
        context['youtube_video_id'] = youtube_video_id
        return context

    def get_youtube_video_id(self, url):
        video_id_match = re.search(r'(?:youtube\.com\/(?:[^\/\n\s]+\/\S+\/|(?:v|e(?:mbed)?)\/|\S*?[?&]v=)|youtu\.be\/)([a-zA-Z0-9_-]{11})', url)
        if video_id_match:
            return video_id_match.group(1)
        return None




    


    

    