from django.db import models

from django.db import models

class Task(models.Model):
    employee_name = models.CharField(max_length=100, default='')
    client_name = models.CharField(max_length=100, default='')
    location = models.CharField(max_length=100, default='')
    task_name = models.CharField(max_length=100, default='')
    time = models.DateField()

class Material(models.Model):
    name = models.CharField(max_length=50, default='')
    code = models.CharField(max_length=10, default='')
    quantity = models.PositiveIntegerField()
    manufacturer = models.CharField(max_length=50, default='')
    date = models.DateField()

class Document(models.Model):
    title = models.CharField(max_length=255)
    file = models.FileField(upload_to='documents/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

def __str__(self):
    return self.name
