from django.db import models

class VideoModel(models.Model):
    video_title = models.CharField(max_length=50)
    video_content = models.FileField(upload_to='videos')
    user = models.IntegerField()
    like = models.IntegerField(default=0)
    dislike = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.video_title

    class Meta:
        verbose_name = 'Video'
        verbose_name_plural = 'Videos'

class User(models.Model):
    user_name = models.CharField(max_length=20)
    phone_number = models.IntegerField()
    email = models.EmailField(max_length=300, unique=True)
    password = models.CharField(max_length=20)
    password2 = models.CharField(max_length=20)