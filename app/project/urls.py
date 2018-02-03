from django.urls import path
from . import views

urlpatterns = [
    path('', views.default, name='index'),
    path('<username>/<project_name>', views.details, name='details')
]