from django import forms
from .models import Task
from .models import Material
from .models import Invoice

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

class InvoiceForm(forms.ModelForm):
    class Meta:
        model = Invoice
        fields = ['customer_name', 'invoice_number', 'invoice_date', 'item_purchased', 'details']
        widgets = {
            'customer_name': forms.TextInput(attrs={'class': 'form-control'}),
            'invoice_number': forms.TextInput(attrs={'class': 'form-control'}),
            'invoice_date': forms.TextInput(attrs={'class': 'form-control'}),
            'item_purchased': forms.TextInput(attrs={'class': 'form-control'}),
            'details': forms.TextInput(attrs={'class': 'form-control'}),
        }