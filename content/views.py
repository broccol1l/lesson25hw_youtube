from django.shortcuts import render
from .models import VideoModel

def home_page(request):
    video = VideoModel.objects.all()
    context = {'video': video}
    return render(request, 'index.html', context=context)

def video_page(request):
    video = VideoModel.objects.all()
    context = {'video': video}
    return render(request, 'video.html', context=context)
