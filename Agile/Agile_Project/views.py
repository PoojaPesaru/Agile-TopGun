from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from .forms import TaskForm
from .models import Task
#from .forms import DocumentForm
from .models import Document

#dashboard view
def dashboard(request):
    return render(request, 'dashboard.html')

#Material Tracking
def material_tracking(request):

    return render(request, 'materialTrackingList.html')

def document_list(request):

    return render(request, 'documentList.html')

#Tasks list
def task_list(request):
    tasks = Task.objects.all()
    print(tasks)

    return render(request, 'TaskSchedular.html', {'tasks': tasks})

#add new material
def add_material(request):

        return render(request, 'materialTracking.html')

#add new task
def add_task(request):
    if request.method == 'POST':
        employee_name = request.POST['employee_name']
        client_name = request.POST['client_name']
        location = request.POST['location']
        task_name = request.POST['task_name']
        new_task = Task(employee_name=employee_name, client_name=client_name, location=location, task_name=task_name)
        new_task.save()
        return render(request, 'TaskSchedular.html')
    else:
        return render(request, 'TaskSchedular.html')



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