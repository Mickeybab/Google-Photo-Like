from django.db import models

# Create your models here.

class Album(models.Model):
    title = models.CharField('Album Title', max_length=120)
    description = models.CharField('Album Description', max_length=1000)
    path = models.CharField('Album Path', max_length=200)
    cover = models.CharField('Album Cover Name', max_length=120)