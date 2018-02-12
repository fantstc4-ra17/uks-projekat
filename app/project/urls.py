from django.urls import path
from . import views

app_name = 'project'
urlpatterns = [
    path('', views.ProjectListView.as_view(), name='project_list'),
    path('start', views.ProjectCreateView.as_view(), name='project_start'),
    path('update/<pk>', views.ProjectUpdateView.as_view(), name='project_update'),
    path('delete/<pk>', views.ProjectDeleteView.as_view(), name='project_delete'),
    path('detail/<pk>', views.ProjectDetailView.as_view(), name='project_detail'),
    path('detail/<pk>/add_milestone', views.MilestoneCreateView.as_view(), name='milestone_add'),
    path('milestone/<pk>', views.MilestoneDetailView.as_view(), name='milestone_detail'),
    path('milestone/update/<pk>', views.MilestoneUpdateView.as_view(), name='milestone_update'),
    path('milestone/delete/<pk>', views.MilestoneDeleteView.as_view(), name='milestone_delete'),
    path('detail/<pk>/add_version', views.VersionCreateView.as_view(), name='version_add'),
    path('version/<pk>', views.VersionDetailView.as_view(), name='version_detail'),
    path('version/update/<pk>', views.VersionUpdateView.as_view(), name='version_update'),
    path('version/delete/<pk>', views.VersionDeleteView.as_view(), name='version_delete'),
]