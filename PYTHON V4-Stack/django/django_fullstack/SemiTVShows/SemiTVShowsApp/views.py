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

def show_new(request):
    return render(request,'addShow.html')

def create_show(request):
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

def show(request,_id):
    _show = Show.objects.get(id=_id)
    context = {
        'show':_show,
    }
    return render(request,'index.html',context)


def show_edit(request,_id):
    show = Show.objects.get(id=_id)
    context = {
        'show':show,
    }
    return render(request,'Edit.html',context)

def show_update(request,_id):
    if request.method == 'POST':
        show = Show.objects.get(id=_id)
        show.title = request.POST['title']
        show.network = request.POST['network']
        show.desc = request.POST['desc']
        show.releaseDate = request.POST['releaseDate']
        show.save()
    
    return redirect(f'/shows/{_id}')

def show_destory(request,_id):
    show = Show.objects.get(id=_id)
    show.delete()

    return redirect('/shows')


