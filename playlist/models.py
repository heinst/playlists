from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Playlist(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

class Tag(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

class TagInstance(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
