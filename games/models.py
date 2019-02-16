from django.db import models

class Game(models.Model):
    image = models.ImageField(upload_to='images/')
    urlname = models.CharField(max_length=200)
    summary = models.CharField(max_length=200)
