from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Field
from .models import Project, Milestone, Version


class ProjectForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(ProjectForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-projectForm'
        self.helper.form_class = 'form-group offset-4'
        self.helper.label_class = 'col-lg-4 font-weight-bold'
        self.helper.field_class = 'col-lg-6'
        self.helper.form_method = 'post'
        self.helper.form_action = 'start'

        self.helper.add_input(Submit('submit', 'Submit'))

    class Meta:
        model = Project
        fields = ['name', 'description',]
    
class MilestoneForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(MilestoneForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-milestoneForm'
        self.helper.form_class = 'form-group offset-4'
        self.helper.label_class = 'col-lg-4 font-weight-bold'
        self.helper.field_class = 'col-lg-6'
        self.helper.form_method = 'post'
        self.helper.form_action = 'add_milestone'

        self.helper.add_input(Submit('submit', 'Submit'))

    class Meta:
        model = Milestone
        fields = ['name', 'description', 'due_date',]

class VersionForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(VersionForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-versionForm'
        self.helper.form_class = 'form-group offset-4'
        self.helper.label_class = 'col-lg-4 font-weight-bold'
        self.helper.field_class = 'col-lg-6'
        self.helper.form_method = 'post'
        self.helper.form_action = 'add_version'

        self.helper.add_input(Submit('submit', 'Submit'))
    class Meta:
        model = Version
        fields = ['name',]
