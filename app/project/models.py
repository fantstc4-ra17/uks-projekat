from django.db import models
from django.conf import settings

# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=50)
    #waiting on user owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    description = models.TextField()
    date_created = models.DateField('date created',auto_now_add=True)
    def __str__(self):
        return self.name + '$user'


class Milestone(models.Model):
    title = models.CharField(max_length=50)
    due_date = models.DateField('due date')
    description = models.TextField()

    def __str__(self):
        return self.title


class Version(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
