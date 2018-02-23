from django import forms
from django.contrib.auth.models import User
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Field
from .models import Project, Milestone, Version


class ProjectForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(ProjectForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-projectForm'
        self.helper.form_class = 'd-table mx-auto justify-content-sm-center'
        self.helper.label_class = 'font-weight-bold'
        self.helper.field_class = 'form-control-sm'
        self.helper.form_group_wrapper_class = 'w-100'
        self.helper.form_method = 'post'
        self.helper.form_action = ''

        self.helper.add_input(Submit('submit', 'Submit'))

    class Meta:
        model = Project
        fields = ['name', 'description',]

class AddMemberForm(forms.Form):

    username = forms.SlugField(max_length=150)

    def __init__(self, *args, **kwargs):
        super(AddMemberForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-addMemberForm'
        self.helper.form_class = 'd-table mx-auto justify-content-sm-center'
        self.helper.label_class = 'font-weight-bold'
        self.helper.field_class = 'form-control-sm'
        self.helper.form_group_wrapper_class = 'w-100'
        self.helper.form_method = 'post'
        self.helper.form_action = ''

        self.helper.add_input(Submit('submit', 'Submit'))

    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username=username).exists():
            return username
        else:
            raise forms.ValidationError('User: %s does not exist.' % username)

    
class MilestoneForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(MilestoneForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-milestoneForm'
        self.helper.form_class = 'd-table mx-auto justify-content-sm-center'
        self.helper.label_class = 'font-weight-bold'
        self.helper.field_class = 'form-control-sm'
        self.helper.form_group_wrapper_class = 'w-100'
        self.helper.form_method = 'post'
        self.helper.form_action = ''

        self.helper.add_input(Submit('submit', 'Submit'))

    class Meta:
        model = Milestone
        fields = ['name', 'description', 'due_date']
        widgets = {
            'due_date': forms.TextInput( attrs = {'type': 'date'} )
        }

class VersionForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(VersionForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-versionForm'
        self.helper.form_class = 'd-table mx-auto justify-content-sm-center'
        self.helper.label_class = 'font-weight-bold'
        self.helper.field_class = 'form-control-sm'
        self.helper.form_group_wrapper_class = 'w-100'
        self.helper.form_method = 'post'
        self.helper.form_action = ''

        self.helper.add_input(Submit('submit', 'Submit'))

    class Meta:
        model = Version
        fields = ['name',]
