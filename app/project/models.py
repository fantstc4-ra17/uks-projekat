from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from .managers import ProjectManager


def default_user():
    try:
        return User.objects.get(username='GhostUser')
    except :
        return User.objects.create_user(username='GhostUser', email='ghost.user@ukshub.com', password='some password')


class Project(models.Model):

    owner = models.ForeignKey(to=User, on_delete=models.CASCADE, default=default_user, related_name="owned_projects", blank=False)
    members = models.ManyToManyField(to=User, related_name='member_of_projects')
    name = models.CharField(max_length=100)
    description = models.TextField()
    date_created = models.DateField('Date created',auto_now_add=True)

    objects = ProjectManager()

    class Meta:
        unique_together = (("owner", "name"),)

    def get_absolute_url(self):
        return reverse('project:project_detail', kwargs={'pk': self.pk})

    def __str__(self):
        return "%s (%s)" % (self.name, self.owner)

class Milestone(models.Model):
    project = models.ForeignKey(to=Project, on_delete=models.CASCADE, related_name='milestones', blank=False)
    name = models.CharField(max_length=100)
    due_date = models.DateField('Due date')
    description = models.TextField()

    class Meta:
        unique_together = (("project", "name"),)

    def get_absolute_url(self):
        return reverse('project:milestone_detail', kwargs={'pk': self.pk})

    def __str__(self):
        return "Milestone: %s (%s)" % (self.name, self.project.name)

class Version(models.Model):
    project = models.ForeignKey(to=Project, on_delete=models.CASCADE, related_name='versions', blank=False)
    name = models.CharField(max_length=100)

    class Meta:
        unique_together = (("project", "name"),)

    def get_absolute_url(self):
        return reverse('project:version_detail', kwargs={'pk': self.pk})
    
    def __str__(self):
        return "Version: %s (%s)" % (self.name, self.project.name)
