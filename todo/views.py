from django.shortcuts import render

def index(request):
    return render(request, 'todo/index.html')

def login(request):
    return render(request, 'todo/login.html')
