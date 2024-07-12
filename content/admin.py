from django.contrib import admin

from .models import VideoModel

@admin.register(VideoModel)
class VideoModelAdmin(admin.ModelAdmin):
    search_fields = ['video_title']
    list_display = ['id', 'video_title', 'user', 'like', 'dislike', 'created_at' ]
    list_filter = ['created_at']
    ordering = ['-id']

