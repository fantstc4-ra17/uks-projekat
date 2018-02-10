from django.test import TestCase
from django.contrib.auth.models import User
from project.views import ProjectCreateView, ProjectDeleteView, ProjectUpdateView
from project.models import Project, default_user


class ProjectViewTest(TestCase):

    @classmethod
    def setUpTestData(self):
        User.objects.create_user('test_user', 'test@test.project', 'some password')
        Project.objects.create_project(name='test project 1')
        Project.objects.create_project(name='test project 2')
    
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
