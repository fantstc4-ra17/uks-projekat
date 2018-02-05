from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.http import HttpResponse
from .models import Project

# Create your views here.
def default(request):
    return HttpResponse('default response')

def index(request):
    project_list = Project.objects.all()
    context = { 
        'project_list': project_list, 
        }
    return render(request, 'project/index.html', context)

def details(request, project_name):
    # when db is populated:
    project = get_object_or_404(Project, name=project_name)
    context = { 
        'project': project_name 
        }
    return render(request, 'project/details.html', context)

def start(request, username):
    return HttpResponse("Start project for user: %s" % username)

def invite(request, username, project_name):
    return HttpResponse("Project %s of user %s invite page." % (project_name, username))
