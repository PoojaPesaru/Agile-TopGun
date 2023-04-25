from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from .forms import TaskForm
from .models import Task
#from .forms import DocumentForm
from .models import Document

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

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

#dashboard view
def dashboard(request):
    user = request.user # access the user object using request.user
    return render(request, 'dashboard.html', {'user': user})


#logout view
def logout_view(request):
    logout(request)
    return redirect('dashboard') # Replace 'login' with the URL name of your app's login page

#Material Tracking
def material_tracking(request):

    return render(request, 'materialTrackingList.html')

def document_list(request):

    return render(request, 'documentList.html')

#Tasks list
def task_list(request):
    tasks = Task.objects.all()
    for task in tasks:
        print(task.employee_name)
        print(task.client_name)
        print(task.location)
        print(task.task_name)
        print(task.time)
    return render(request, 'TaskSchedular.html', {'tasks': tasks})

#Task Detail View

#add new material
def add_material(request):

        return render(request, 'materialTracking.html')

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



#def upload_document(request):
  #  if request.method == 'POST':
   #     form = DocumentForm(request.POST,request.FILES)
    #    if form.is_valid():
     #       form.save()
      #      return HttpResponseRedirect(reverse('document_list'))
  #  else:
      #  form = DocumentForm()

  #  return render(request, 'upload_document.html', {'form': form})


#def document_list(request):
   # documents = Document.objects.all()
  #  return render(request, 'document_list.html', {'documents': documents})