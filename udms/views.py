from django.shortcuts import render
from django.http import HttpResponse

def dashboard(request):
    context = {
        'message': 'Welcome to the University Disciplinary Management System!..'
    }
    return render(request, 'dashboard.html', context)
