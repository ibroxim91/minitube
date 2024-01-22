from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class User(AbstractUser):
    phone = models.CharField(max_length=13, verbose_name="Phone" , blank=True)
    image = models.ImageField(upload_to="user_images")
    followings = models.ManyToManyField('self')
    liked_videos = models.ManyToManyField('main.VideoContent', related_name="user_liked_videos")
    watched_videos = models.ManyToManyField('main.VideoContent')





