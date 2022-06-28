from django.shortcuts import render
from time import localtime, strftime


def index(request):
    context = {
        "time": strftime("%H:%M %p ", localtime()),
        "date": strftime("%b %d , %Y ", localtime())
    }
    return render(request,'index.html', context)