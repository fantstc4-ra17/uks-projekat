from django.urls import path
from . import views

app_name = 'project'
urlpatterns = [
    path('', views.ProjectListView.as_view(), name='project_list'),
    path('start', views.ProjectCreateView.as_view(), name='project_start'),
    path('update/<pk>', views.ProjectUpdateView.as_view(), name='project_update'),
    path('delete/<pk>', views.ProjectDeleteView.as_view(), name='project_delete'),
    path('detail/<pk>', views.ProjectDetailView.as_view(), name='project_detail'),
    #future path(maybe): path('<username>/<project_name>', views.details, name='details'),
]