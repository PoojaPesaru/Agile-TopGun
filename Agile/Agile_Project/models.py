from django.db import models

class Task(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    owner = models.CharField(max_length=200)
    status_choices = (
        ('todo', 'To Do'),
        ('inprogress', 'In Progress'),
        ('done', 'Done'),
    )
    status = models.CharField(max_length=20, choices=status_choices, default='todo')
    due_date = models.DateField()
    time = models.TimeField()

class Document(models.Model):
    title = models.CharField(max_length=255)
    file = models.FileField(upload_to='documents/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

def __str__(self):
    return self.name
