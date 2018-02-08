from django.db import models

### MANAGERS

class ProjectManager(models.Manager):
    def create_project(self, name, description=''):
        project = self.create(name=name, description=description)
        return project