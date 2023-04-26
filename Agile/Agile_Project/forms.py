from django import forms
from .models import Task
from .models import Material

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

class MaterialForm(forms.ModelForm):
    class Meta:
        model = Material
        fields = ['name', 'code', 'quantity', 'manufacturer', 'date']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'})
        }
