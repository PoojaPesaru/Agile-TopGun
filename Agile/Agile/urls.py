"""Agile URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
import Agile_Project.views

urlpatterns = [
    path('', Agile_Project.views.dashboard, name='dashboard'),
    path('register/', Agile_Project.views.registration_view, name='registration_view'),
    path('login/', Agile_Project.views.login_view, name='login'),
    path('logout/', Agile_Project.views.logout_view, name='logout'),
    path('task-list/', Agile_Project.views.task_list, name='task_list'),
    path('add-task/', Agile_Project.views.add_task, name='add_task'),
    path('tasks/<int:task_id>/', Agile_Project.views.task_detail, name='task_detail'),
    path('material-tracking/', Agile_Project.views.material_tracking, name='material_tracking'),
    path('materials/<int:material_id>/', Agile_Project.views.material_detail, name='material_detail'),
    path('add-material/', Agile_Project.views.add_material, name='add_material'),
    path('document-list/', Agile_Project.views.document_list, name='document_list'),
    path('upload/', Agile_Project.views.upload_document, name='upload_document'),
]

