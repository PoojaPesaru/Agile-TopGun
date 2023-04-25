from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['employee_name', 'client_name', 'location', 'task_name', 'time']
        labels = {
            'employee_name': 'Employee Name',
            'client_name': 'Client Name',
            'location': 'Location',
            'task_name': 'Task',
            'time': 'Time'
        }
        widgets = {
            'time': forms.DateInput(attrs={'type': 'date'})
        }
