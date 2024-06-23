# crm_system/views.py
from django.shortcuts import render

def home_view(request):
    return render(request, 'home.html')

from django.shortcuts import render

def serve_react_app(request):
    return render(request, 'index.html')