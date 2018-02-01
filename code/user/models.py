from django.db import models
# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    picture_url = models.URLField()
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
