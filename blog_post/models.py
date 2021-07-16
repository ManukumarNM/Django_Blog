from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse
# from PIL import Image

class Post(models.Model):
    post_author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    content = models.TextField()
    post_date = models.DateTimeField(default=timezone.now)
    image = models.ImageField(upload_to='post_pics', blank=True, null=True)


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.id)])


    