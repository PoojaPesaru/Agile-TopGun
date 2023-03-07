# path -> listings/views.py

from django.shortcuts import render

def login_page(request):

    return render(request, 'listings/login_page.html')
