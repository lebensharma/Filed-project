from django.db import models
from django.db.models.signals import post_delete
from django.dispatch import receiver


# Create your models here.
class Song(models.Model):
    id = models.AutoField(primary_key=True)
    type = models.TextField(editable=False, default='song')
    name = models.TextField(max_length=100)
    file = models.FileField(upload_to='songs')
    duration = models.CharField(max_length=50)
    timeupload = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name


class Podcast(models.Model):
    id = models.AutoField(primary_key=True)
    type = models.TextField(editable=False, default='podcast')
    name = models.TextField(max_length=100)
    file = models.FileField(upload_to='podcasts')
    duration = models.CharField(max_length=50)
    host = models.TextField(max_length=100)
    participants = models.CharField(max_length=1010)
    timeupload = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name + ' hosted by ' + self.host


class Audiobook(models.Model):
    id = models.AutoField(primary_key=True)
    type = models.TextField(editable=False, default='audiobook')
    title = models.TextField(max_length=100)
    author = models.TextField(max_length=100)
    narrator = models.TextField(max_length=100)
    file = models.FileField(upload_to='audiobooks')
    duration = models.CharField(max_length=50)
    timeupload = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title + ' by ' + self.author
