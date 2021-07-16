from django.contrib import admin
from django.contrib.admin.options import ModelAdmin
from .models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = ['post_author', 'title', 'content', 'post_date', 'image']

admin.site.register(Post, PostAdmin)