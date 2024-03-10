from django.db.models.base import Model as Model
from django.db.models.query import QuerySet
from django.shortcuts import render
import re
from django.views.generic import DetailView
from .models import Video

#URLを埋め込みコードに変換
def get_youtube_video_id(url):
    video_id_match = re.search(r'(?:youtube\.com\/(?:[^\/\n\s]+\/\S+\/|(?:v|e(?:mbed)?)\/|\S*?[?&]v=)|youtu\.be\/)([a-zA-Z0-9_-]{11})', url)
    if video_id_match:
        return video_id_match.group(1)
    return None

#フロントに送信
#URLがあるときとないときをif文で
def youtube_embed(request):
    youtube_urls = Video.objects.all()
    for youtube_url in youtube_urls:
        video_id = get_youtube_video_id(youtube_url.video_url)
        
    return render(request, 'ren_app/youtube_embed.html', {'video_id': video_id})

#詳細画面
class DetaiVideoView(DetailView):
    template_name = 'ren_app/detail.html'
    model = Video

    def get_object(self, queryset=None):
        # ここで適切なオブジェクトを取得するロジックを実装します。
        return Video.objects.get(pk=self.kwargs['pk'])


    

    