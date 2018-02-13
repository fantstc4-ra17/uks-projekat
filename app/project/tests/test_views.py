from django.test import TestCase, Client
from unittest import skip
from django.contrib.auth.models import User
from guardian.shortcuts import assign_perm
from project.views import ProjectCreateView, ProjectDeleteView, ProjectUpdateView
from project.models import Project, Milestone, Version, default_user


class ProjectViewTest(TestCase):

    @classmethod
    def setUpTestData(self):
        owner = User.objects.create_user('test_user', 'test@test.project', 'some password')
        project_1 = Project.objects.create_project(name='test project 1')
        project_2 = Project.objects.create_project(name='test project 2')
        project_1.owner = owner
        project_2.owner = owner
        project_1.save()
        project_2.save()
        assign_perm("delete_project", owner, project_1)
        assign_perm("delete_project", owner, project_2)
        assign_perm("change_project", owner, project_1)
        assign_perm("change_project", owner, project_2)
        
    
    def test_project_create(self):
        self.client.login(username='test_user', password='some password')
        test_url = '/project/start'
        response = self.client.get(test_url)
        self.assertEquals(response.status_code, 200)
        response = self.client.post(test_url, {'name': 'testt1', 'description': 'test description'})
        self.assertEquals(response.status_code, 302)
        test_project = Project.objects.get(name='testt1')
        self.assertEquals(test_project.owner.username, 'test_user')

    def test_project_detail(self):
        test_url = '/project/detail/'
        response = self.client.get(test_url+'1')
        self.assertEquals(response.status_code, 200)
        response = self.client.get(test_url+'2')
        self.assertEquals(response.status_code, 200)
    
    def test_project_update(self):
        self.client.login(username='test_user', password='some password')
        test_url = '/project/update/1'
        response = self.client.get(test_url)
        self.assertEquals(response.status_code, 200)
        new_name = 'test1 updated'
        response = self.client.post(test_url, {'name': new_name, 'description': 'updated description'})
        test_project = Project.objects.get(pk=1)
        self.assertEquals(test_project.name, new_name)

    def test_project_delete(self):
        self.client.login(username='test_user', password='some password')
        test_url = '/project/delete/2'
        response = self.client.get(test_url)
        self.assertEquals(response.status_code, 200)
        response = self.client.post(test_url)
        with self.assertRaises(Project.DoesNotExist):
            Project.objects.get(pk=2)

    def test_milestone_create_update_delete(self):
        self.client.login(username='test_user', password='some password')
        test_url = '/project/detail/1/add_milestone'
        response = self.client.get(test_url)
        self.assertEquals(response.status_code, 200)
        response = self.client.post(test_url, {'name': 'milestone_test', 'description': 'test description', 'due_date': '10/10/2018'})
        self.assertEquals(response.status_code, 302)
        test_milestone = Milestone.objects.get(name='milestone_test')
        self.assertEquals(test_milestone.project.id, 1)

        test_url = '/project/milestone/update/1'
        response = self.client.get(test_url)
        self.assertEquals(response.status_code, 200)
        new_name = 'test1 milestone updated'
        response = self.client.post(test_url, {'name': new_name, 'description': 'updated description', 'due_date': '11/11/2019'})
        test_milestone = Milestone.objects.get(pk=1)
        self.assertEquals(test_milestone.name, new_name)

        test_url = '/project/milestone/delete/1'
        response = self.client.get(test_url)
        self.assertEquals(response.status_code, 200)
        response = self.client.post(test_url)
        with self.assertRaises(Milestone.DoesNotExist):
            Milestone.objects.get(pk=1)

    def test_version_create_update_delete(self):
        self.client.login(username='test_user', password='some password')
        test_url = '/project/detail/1/add_version'
        response = self.client.get(test_url)
        self.assertEquals(response.status_code, 200)
        response = self.client.post(test_url, {'name': 'version_test'})
        self.assertEquals(response.status_code, 302)
        test_version = Version.objects.get(name='version_test')
        self.assertEquals(test_version.project.id, 1)

        test_url = '/project/version/update/1'
        response = self.client.get(test_url)
        self.assertEquals(response.status_code, 200)
        new_name = 'test1 version updated'
        response = self.client.post(test_url, {'name': new_name})
        test_version = Version.objects.get(pk=1)
        self.assertEquals(test_version.name, new_name)

        test_url = '/project/version/delete/1'
        response = self.client.get(test_url)
        self.assertEquals(response.status_code, 200)
        response = self.client.post(test_url)
        with self.assertRaises(Version.DoesNotExist):
            Version.objects.get(pk=1)