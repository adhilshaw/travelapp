from django.db import models


# Create your models here.
class Place(models.Model):

    objects = None
    name = models.CharField(max_length=250)
    img = models.ImageField(upload_to='pics')
    desc = models.TextField()


class Team(models.Model):
    objects = None
    names = models.CharField(max_length=250)
    imgs = models.ImageField(upload_to='pics')
    descs = models.TextField()
