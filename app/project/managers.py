from django.db import models

### MANAGERS

class ProjectManager(models.Manager):
    def create_project(self, name):
        project = self.create(name=name)
        return project