from django.shortcuts import render
from django.http import HttpResponse
from .EngineCKB import Engine


def home(request):
    return render(request, 'page/page.html')


def thread(request):
    return render(request, 'page/thread.html')


def about(request):
    return render(request, 'page/aboutus.html')


def result(request):
    if request.method == 'POST':
        test = request.POST["search"]
        engine = Engine(test)
        print(engine.res)
    return render(request, 'page/result.html', {'engine': engine.res})
