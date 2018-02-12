from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from guardian.mixins import PermissionRequiredMixin
from guardian.shortcuts import assign_perm
from .models import Project, Version, Milestone
from .forms import ProjectForm, VersionForm, MilestoneForm

# Create your views here.

class ProjectCreateView(LoginRequiredMixin, CreateView):
    model = Project
    form_class = ProjectForm
    template_name_suffix = '_create_form'
    context_object_name = 'project'

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return_value = super().form_valid(form)
        assign_perm("delete_project", self.request.user, form.instance)
        assign_perm("change_project", self.request.user, form.instance)
        return return_value

class ProjectUpdateView(PermissionRequiredMixin, UpdateView):
    model = Project
    form_class = ProjectForm
    template_name_suffix = '_update_form'
    context_object_name = 'project'
    permission_required = 'change_project'

class ProjectDeleteView(PermissionRequiredMixin, DeleteView):
    model = Project
    success_url = reverse_lazy('project:project_list')
    context_object_name = 'project'
    permission_required = 'delete_project'

class ProjectListView(ListView):
    model = Project
    context_object_name = 'project_list'
    queryset = Project.objects.all()

class ProjectDetailView(DetailView):
    model = Project
    context_object_name = 'project'
    