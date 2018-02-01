"""views for user app"""

from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    """index of users."""
    return HttpResponse("User page stub.")
