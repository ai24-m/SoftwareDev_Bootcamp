from django.db import models

class Dojo(models.Model):
    name = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state= models.CharField(max_length=2)
    desc=models.TextField(default='old dojo')

class Ninjas(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    dojo_id= models.ForeignKey(Dojo,related_name='dojo', on_delete=models.CASCADE )