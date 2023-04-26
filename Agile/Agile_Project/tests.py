from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from django.urls import reverse
from models import Task, Document, Material
from forms import TaskForm
from django.core.files.uploadedfile import SimpleUploadedFile
from datetime import date, time

class TaskSchedulerTestCase(TestCase):

    def setUp(self):
        self.task = Task.objects.create(
            name='Task 1',
            description='Description of Task 1',
            owner='Owner 1',
            status='todo',
            due_date=date.today(),
            time=time(hour=9, minute=0)
        )
        self.document = Document.objects.create(
            title='Document 1',
            file=SimpleUploadedFile("test.txt", b"file_content"),
            uploaded_at=date.today()
        )

    def test_add_task_view(self):
        url = reverse('add_task')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'add_task.html')
        self.assertIsInstance(response.context['form'], TaskForm)

        data = {
            'name': 'Task 2',
            'description': 'Description of Task 2',
            'owner': 'Owner 2',
            'status': 'todo',
            'due_date': date.today(),
            'time': time(hour=9, minute=0)
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302) # Redirects to task_list page
        self.assertRedirects(response, reverse('task_list'))

    def test_task_list_view(self):
        url = reverse('task_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'task_list.html')
        self.assertQuerysetEqual(response.context['tasks'], ['<Task: Task 1>'])



    def test_document_list_view(self):
        url = reverse('document_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'document_list.html')
        self.assertQuerysetEqual(response.context['documents'], ['<Document: Document 1>'])





    #Test case for material tracking view:
    def test_material_tracking_view(self):
        # create some test materials
        Material.objects.create(name='Material 1', code='M001')
        Material.objects.create(name='Material 2', code='M002')
        Material.objects.create(name='Material 3', code='M003')
        # create a GET request to the material tracking view
        response = self.client.get('/material_tracking/')
        # check that the response status code is 200 (OK)
        self.assertEqual(response.status_code, 200)
        # check that all materials are included in the response
        self.assertEqual(len(response.context['materials']), 3)

    #Test case for adding a new material:
    def test_add_material_view(self):
        # create a POST request with valid form data
        response = self.client.post('/add_material/', {'name': 'Test Material', 'code': 'TM001'})
        # check that the response status code is 302 (redirect)
        self.assertEqual(response.status_code, 302)
        # check that the material was created
        self.assertTrue(Material.objects.filter(name='Test Material').exists())
        # check that the user is redirected to the material tracking view
        self.assertRedirects(response, '/material_tracking/')


