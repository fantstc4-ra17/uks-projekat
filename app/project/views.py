from django.shortcuts import render, get_object_or_404 
from django.http import HttpResponse
from .models import Project

# Create your views here.
def default(request):
    return HttpResponse('default response')

def details(request, username, project_name):
    # when db is populated:
    # project = get_object_or_404(Project, name=project_name)
    project = ''
    context={'username': username}
    return render(request, 'project/details.html', context)

def start(request, username):
    return HttpResponse("Start project for user: %s" % username)

def invite(request, username, project_name):
    return HttpResponse("Project %s of user %s invite page." % (project_name, username))
