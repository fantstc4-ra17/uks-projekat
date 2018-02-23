from django import forms
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, AnonymousUser
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView, ModelFormMixin
from django.views.generic.detail import DetailView, SingleObjectMixin
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from guardian.mixins import PermissionRequiredMixin
from guardian.shortcuts import assign_perm
from .models import Project, Version, Milestone
from .forms import ProjectForm, AddMemberForm, VersionForm, MilestoneForm

class HomePageView(ListView):

    model = Project
    template_name = 'index.html'
    context_object_name = 'users_projects'

    def get_queryset(self):
        if isinstance(self.request.user, User):
            return Project.objects.filter(owner = self.request.user).order_by('-date_created')[:10]

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        context['num_projects'] = Project.objects.all().count()
        context['num_users'] = User.objects.all().count()
        return context
        

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


class ProjectMemberAddView(FormView, SingleObjectMixin, PermissionRequiredMixin):
    form_class = AddMemberForm
    model = Project
    template_name = 'project/project_member_add_form.html'
    context_object_name = 'project'
    permission_required = 'change_project'

    def form_valid(self, form):
        member_username = form.cleaned_data['username']
        member = User.objects.get(username=member_username)
        self.object.members.add(member)
        self.object.save()
        return redirect(self.get_success_url())

    def get_success_url(self):
        project_id = self.kwargs['pk']
        return reverse_lazy('project:project_detail', args=[project_id])

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().get(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().post(request, *args, **kwargs)


class ProjectMemberDeleteView(DeleteView, PermissionRequiredMixin):
    model = Project
    template_name = 'project/project_member_confirm_remove.html'

    def delete(self, request, *args, **kwargs):
        project = self.get_object()
        project.members.remove(self.get_user_object(pk=self.kwargs['upk']))
        return redirect(self.get_success_url())

    def get_success_url(self):
        project_id = self.kwargs['pk']
        return reverse_lazy('project:project_detail', args=[project_id])
    
    def get_user_object(self, pk):
        return User.objects.get(pk=pk)

class MilestoneCreateView(LoginRequiredMixin, CreateView):
    model = Milestone
    form_class = MilestoneForm
    template_name_suffix = '_create_form'
    context_object_name = 'milestone'

    def form_valid(self, form):
        project_id = self.kwargs['pk']
        form.instance.project = Project.objects.get(id=project_id)
        return_value = super().form_valid(form)
        assign_perm("delete_milestone", self.request.user, form.instance)
        assign_perm("change_milestone", self.request.user, form.instance)
        return return_value

class MilestoneUpdateView(PermissionRequiredMixin, UpdateView):
    model = Milestone
    form_class = MilestoneForm
    template_name_suffix = '_update_form'
    context_object_name = 'milestone'
    permission_required = 'change_milestone'

class MilestoneDeleteView(PermissionRequiredMixin, DeleteView):
    model = Milestone
    context_object_name = 'milestone'
    permission_required = 'delete_milestone'

    def get_success_url(self):
        return reverse_lazy('project:project_detail', kwargs={'pk': self.get_object().project.id})

class MilestoneListView(ListView):
    model = Milestone
    context_object_name = 'milestone_list'
    queryset = Project.objects.all()

class MilestoneDetailView(DetailView):
    model = Milestone
    context_object_name = 'milestone'
    
class VersionCreateView(LoginRequiredMixin, CreateView):
    model = Version
    form_class = VersionForm
    template_name_suffix = '_create_form'
    context_object_name = 'version'

    def form_valid(self, form):
        project_id = self.kwargs['pk']
        form.instance.project = Project.objects.get(id=project_id)
        return_value = super().form_valid(form)
        assign_perm("delete_version", self.request.user, form.instance)
        assign_perm("change_version", self.request.user, form.instance)
        return return_value

class VersionUpdateView(PermissionRequiredMixin, UpdateView):
    model = Version
    form_class = VersionForm
    template_name_suffix = '_update_form'
    context_object_name = 'version'
    permission_required = 'change_version'

class VersionDeleteView(PermissionRequiredMixin, DeleteView):
    model = Version
    context_object_name = 'version'
    permission_required = 'delete_version'

    def get_success_url(self):
        return reverse_lazy('project:project_detail', kwargs={'pk': self.get_object().project.id})

class VersionListView(ListView):
    model = Version
    context_object_name = 'Version_list'
    queryset = Project.objects.all()

class VersionDetailView(DetailView):
    model = Version
    context_object_name = 'version'