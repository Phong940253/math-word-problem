from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request, 'page/page.html')

def thread(request):
    return render(request, 'page/thread.html')

def about(request):
    return render(request, 'page/aboutus.html')