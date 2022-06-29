from django.shortcuts import render, redirect
from .models import *

def index(request):
    return redirect('/shows')

def shows(request):
    shows = Show.objects.all()
    context = {
        'shows':shows,
    }
    return render(request,'showPage.html',context)

def addPage(request):
    return render(request,'addShow.html')

def show(request,_id):
    show = Show.objects.get(id=_id)
    context = {
        'show':show,
    }
    return render(request,'index.html',context)



def showEdit(request,_id):
    show = Show.objects.get(id=_id)
    context = {
        'show':show,
    }
    return render(request,'Edit.html',context)


def newShow(request):
    if request.method == 'POST':
        show = Show.objects.create(
            title = request.POST['title'],
            network = request.POST['network'],
            releaseDate = request.POST['releaseDate'],
            desc = request.POST['desc']
        )
        show.save()
        return redirect(f'/shows/{show.id}')
    return redirect('/')


def showUpdate(request,_id):
    if request.method == 'POST':
        show = Show.objects.get(id=_id)
        show.title = request.POST['title']
        show.network = request.POST['network']
        show.desc = request.POST['desc']
        show.releaseDate = request.POST['releaseDate']
        show.save()
    return redirect(f'/shows/{_id}')

def showDestory(request,_id):
    show = Show.objects.get(id=_id)
    show.delete()
    return redirect('/shows')


