from .forms import TaskForm
from .models import Task
from .forms import MaterialForm
from .models import Material
from .forms import InvoiceForm
from .models import Invoice



#from .forms import DocumentForm
from .models import Document

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.core.files.storage import FileSystemStorage

#user registration view
def registration_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login') # Replace 'login' with the URL name of your app's login page
    else:
        form = UserCreationForm()
    return render(request, 'registration.html', {'form': form})

#login view
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request=request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('dashboard') # redirect without argument
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

#logout view
def logout_view(request):
    logout(request)
    return redirect('dashboard') # Replace 'login' with the URL name of your app's login page

#dashboard view
def dashboard(request):
    user = request.user # access the user object using request.user
    return render(request, 'dashboard.html', {'user': user})

#Material Tracking
def material_tracking(request):
    materials = Material.objects.all()
    return render(request, 'materialTrackingList.html',{'materials': materials})

#Task Detail View
def material_detail(request, material_id):
    material = get_object_or_404(Material, pk=material_id)
    print(material.code)
    return render(request, 'MaterialTrackingView.html', {'material': material})

#add new material
def add_material(request):
    if request.method == 'POST':
        form = MaterialForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('material_tracking')
    else:
        form = MaterialForm()
    return render(request, 'materialTracking.html', {'form': form})

#add new task
def add_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm()

    return render(request, 'ShiftSchedular.html', {'form': form})

#Tasks list
def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'TaskSchedular.html', {'tasks': tasks})

#Task Detail View
def task_detail(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    return render(request, 'ShiftSchedularDetail.html', {'task': task})

def invoice_list(request):
    invoices = Invoice.objects.all()
    return render(request, 'invoiceTrackingList.html', {'invoices': invoices})

def add_invoice(request):
    if request.method == 'POST':
        form = InvoiceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('invoice_list')
    else:
        form = InvoiceForm()
    return render(request, 'invoicetrackingform.html', {'form': form})

def upload_document(request):
    if request.method == 'POST' and request.FILES['document']:
        document = request.FILES['document']
        fs = FileSystemStorage()
        fs.save(document.name, document)
        return render(request, 'documentList.html')
    return redirect('document_list')

def document_list(request):
    documents = Document.objects.all()
    return render(request, 'documentList.html', {'documents': documents})