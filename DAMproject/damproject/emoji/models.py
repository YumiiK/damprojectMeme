from django.db import models


class User(models.Model):
    username = models.CharField(max_length=20)
    email = models.EmailField(max_length=40, default='')
    password = models.CharField(max_length=20)
    like_images = models.TextField(default='')


class Image(models.Model):
    classification = models.CharField(default='', max_length=200)
    total_likes = models.IntegerField(default=0)
    tags = models.CharField(default='', max_length=200)
    upload_time = models.DateTimeField(auto_now_add=True)
    img = models.CharField(default='', max_length=200)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, default='')

# Create your models here.
