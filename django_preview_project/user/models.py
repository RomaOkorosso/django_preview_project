from PIL import Image
from django.contrib.auth.models import User
from django.db import models
from django_preview_project import post


# create here user's models depens on basic django user model

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=128, unique=True, blank=True)
    email = models.EmailField(max_length=128, unique=True, blank=True)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    posts = models.ManyToManyField('post.Post', blank=True)
    likes = models.ManyToManyField('post.Like', blank=True)
    dislikes = models.ManyToManyField('post.Dislike', blank=True)
    comments = models.ManyToManyField('post.Comment', blank=True)

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)
