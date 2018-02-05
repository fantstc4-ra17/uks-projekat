from django.db import models
from django.conf import settings
from django.contrib import auth
from django.db.models.signals import post_save
from django.dispatch import receiver
from .managers import ProjectManager

class Project(models.Model):

    @staticmethod
    def default_user():
        return auth.get_user_model().objects.create_user(username='GhostUser', email='ghost.user@ukshub.com', password='some password')

    owner = models.ForeignKey(to=auth.get_user_model(), on_delete=models.CASCADE, default=default_user, related_name="projects",)
    name = models.CharField(max_length=50)
    description = models.TextField()
    date_created = models.DateField('date created',auto_now_add=True)

    objects = ProjectManager()

    @staticmethod
    def default_project():
        return Project.objects.create_project(name='GhostProject')

    def __str__(self):
        return self.name + '$user'

class Milestone(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, default=Project.default_project)
    title = models.CharField(max_length=50)
    due_date = models.DateField('due date')
    description = models.TextField()

    def __str__(self):
        return self.title


class Version(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, default=Project.default_project)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name