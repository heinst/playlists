from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Playlist(models.Model):
    spotify_id = models.CharField(max_length=100)
    description = models.TextField(max_length=600)
    likes = models.IntegerField()
    follows = models.IntegerField()

class Tag(models.Model):
    category = models.CharField(max_length=25)
    name = models.CharField(max_length=25)

class TagInstance(models.Model):
    tag = models.ForeignKey(Tag)
    playlist = models.ForeignKey(Playlist)
