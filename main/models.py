from django.db import models
from accounts.models import User
# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class VideoContent(models.Model):
    author = models.ForeignKey(User, related_name='videos', on_delete=models.CASCADE)
    category = models.ForeignKey(Category, related_name='videos', on_delete=models.PROTECT)
    title = models.CharField(max_length=255)
    file = models.FileField(upload_to="videos", blank=True)

    image = models.ImageField(upload_to="images", blank=True)

    video_url = models.URLField(max_length=255, blank=True)
    text = models.TextField(max_length=500)
    likes = models.PositiveBigIntegerField(default=0)
    dislikes = models.PositiveBigIntegerField(default=0)
    views = models.PositiveBigIntegerField(default=0)
    comments_count = models.PositiveBigIntegerField(default=0)
    reg_date = models.DateTimeField(auto_now_add=True)


class Comment(models.Model):
    author = models.ForeignKey(User, related_name='comments', on_delete=models.CASCADE)
    video = models.ForeignKey(VideoContent, related_name='comments', on_delete=models.CASCADE)
    text = models.TextField(max_length=500)
    reg_date = models.DateTimeField(auto_now_add=True)


