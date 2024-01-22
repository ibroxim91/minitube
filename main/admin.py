from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title']

@admin.register(VideoContent)
class VideoAdmin(admin.ModelAdmin):
    list_display = ['author', "category",'title']
    readonly_fields = ['likes',"dislikes","views","comments_count"]
    list_filter = ("author","category")