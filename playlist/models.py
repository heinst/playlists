from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Playlist(models.Model):

    spotify_id = models.CharField(max_length=30, unique=True)
    # spotify_snapshot = models.CharField(max_length=30)
    # length = models.IntegerField()
    description = models.TextField(max_length=600, default="Description, yo")
    likes = models.IntegerField(default=0)
    follows = models.IntegerField(default=0)
    user_id = models.CharField(max_length=30, null=False)
    name = models.CharField(max_length=100, default="")

class Tag(models.Model):
    category = models.CharField(max_length=25)
    name = models.CharField(max_length=25)

class TagInstance(models.Model):
    tag = models.ForeignKey(Tag)
    playlist = models.ForeignKey(Playlist)
