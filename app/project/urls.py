from django.urls import path
from . import views

app_name = 'project'
urlpatterns = [    
    path('<pk>/detail', views.ProjectDetailView.as_view(), name='project_detail'),
    path('list', views.ProjectListView.as_view(), name='project_list'),
    path('start', views.ProjectCreateView.as_view(), name='project_start'),
    path('<pk>/update', views.ProjectUpdateView.as_view(), name='project_update'),
    path('<pk>/delete', views.ProjectDeleteView.as_view(), name='project_delete'),
    path('<pk>/add-member', views.ProjectMemberAddView.as_view(), name='project_member_add'),
    path('<pk>/remove-member/<upk>', views.ProjectMemberDeleteView.as_view(), name='project_member_remove'),
    path('<pk>/add_milestone', views.MilestoneCreateView.as_view(), name='milestone_add'),
    path('milestone/<pk>', views.MilestoneDetailView.as_view(), name='milestone_detail'),
    path('milestone/<pk>/update', views.MilestoneUpdateView.as_view(), name='milestone_update'),
    path('milestone/<pk>/delete', views.MilestoneDeleteView.as_view(), name='milestone_delete'),
    path('<pk>/add_version', views.VersionCreateView.as_view(), name='version_add'),
    path('version/<pk>', views.VersionDetailView.as_view(), name='version_detail'),
    path('version/<pk>/update', views.VersionUpdateView.as_view(), name='version_update'),
    path('version/<pk>/delete', views.VersionDeleteView.as_view(), name='version_delete'),
]