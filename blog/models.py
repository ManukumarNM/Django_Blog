from django.db import models
from django.contrib.auth.models import User 
from PIL import Image
from django.utils import timezone
from django.urls import reverse

# Author model with its fields
class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='profile_pics/default.jpg', upload_to='profile_pics')

    def get_absolute_url(self):
        return reverse('author-detail', args=[str(self.id)])
        
    def __str__(self):
        return f' Author - {self.user.username}'
    
    
# User contact Model with its attributes   
class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()   
    mobile = models.IntegerField()
    message = models.TextField(max_length=150)

    def __str__(self):
        return self.name


