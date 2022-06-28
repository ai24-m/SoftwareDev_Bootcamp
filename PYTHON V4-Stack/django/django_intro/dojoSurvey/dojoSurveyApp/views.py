from django.shortcuts import render, HttpResponse
from multiprocessing import context
from operator import concat


def index(request):
    return render(request, "index.html")


def result(request):
    _name= request.POST['name']
    _location= request.POST['location']
    _language= request.POST['language']
    _comment= request.POST['comment']

    context = {
        'name': _name,
        'location': _location,
        'language': _language,
        'comment': _comment
    }
    return render(request, "result.html",context )

def goBack(request):
    _goBack= request.POST['goBack']

    context = {
        'goBack': _goBack
    }
    return render(request, "index.html", context)
