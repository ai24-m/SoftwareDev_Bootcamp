
from django.db import models



class Show(models.Model):
    title = models.CharField(max_length=255)
    network = models.CharField(max_length=150)
    desc = models.TextField()
    releaseDate =  models.DateTimeField()
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)


