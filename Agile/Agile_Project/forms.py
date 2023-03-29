from django import forms
from .models import Task
from .models import Document

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['name', 'description', 'owner', 'status', 'due_date', 'time']

class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ['title','file']
