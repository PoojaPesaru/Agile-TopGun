from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from .forms import TaskForm
from .models import Task
from .forms import DocumentForm
from .models import Document

def add_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('task_list'))
    else:
        form = TaskForm()

    return render(request, 'add_task.html', {'form': form})

def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'task_list.html', {'tasks': tasks})

def upload_document(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('document_list'))
    else:
        form = DocumentForm()

    return render(request, 'upload_document.html', {'form': form})


def document_list(request):
    documents = Document.objects.all()
    return render(request, 'document_list.html', {'documents': documents})