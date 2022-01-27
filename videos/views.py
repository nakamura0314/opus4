from django.urls import reverse_lazy
from django.views import generic
from .forms import VideoCreateForm
from .models import Video


# IndexViewはビデオの一覧表示
class IndexView(generic.ListView):
    model = Video


# CreateViewはアップデートページ
class CreateView(generic.CreateView):
    model = Video
    form_class = VideoCreateForm
    success_url = reverse_lazy('videos:index')


# DetailViewは動画の再生ページ
class PlayView(generic.DetailView):
    model = Video
