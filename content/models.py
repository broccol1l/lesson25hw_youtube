from django.db import models
from django.utils import timezone
class VideoModel(models.Model):
    video_title = models.CharField(max_length=50)
    video_content = models.FileField(upload_to='videos')
    user = models.IntegerField()
    like = models.IntegerField(default=0)
    dislike = models.IntegerField(default=0)
    preview = models.FileField(default=timezone.now, upload_to='thumbnails/')
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.video_title

    class Meta:
        verbose_name = 'Video'
        verbose_name_plural = 'Videos'

