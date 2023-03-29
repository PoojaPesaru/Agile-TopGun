from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from django.urls import reverse
from models import Task, Document
from forms import TaskForm, DocumentForm
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

    def test_upload_document_view(self):
        url = reverse('upload_document')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'upload_document.html')
        self.assertIsInstance(response.context['form'], DocumentForm)

        data = {
            'title': 'Document 2',
            'file': SimpleUploadedFile("test.txt", b"file_content")
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302) # Redirects to document_list page
        self.assertRedirects(response, reverse('document_list'))

    def test_document_list_view(self):
        url = reverse('document_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'document_list.html')
        self.assertQuerysetEqual(response.context['documents'], ['<Document: Document 1>'])
