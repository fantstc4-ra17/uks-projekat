from django import forms
from .models import Project, Milestone, Version


class ProjectForm(forms.ModelForm):

    class Meta:
        model = Project
        fields = ['name', 'description',]
    
class MilestoneForm(forms.ModelForm):

    class Meta:
        model = Milestone
        fields = ['title', 'description', 'due_date',]

class VersionForm(forms.ModelForm):

    class Meta:
        model = Version
        fields = ['name',]
