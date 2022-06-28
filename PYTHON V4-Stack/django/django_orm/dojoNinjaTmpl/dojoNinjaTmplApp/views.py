
from django.shortcuts import render,redirect
from dojoNinjaTmplApp.models import Dojo
from .models import *



def index(request):
    # _dojo =Dojo.objects.all()
    context ={
        'dojos':Dojo.objects.all(),
        'ninjas':Ninja.objects.all(),
    }
    return render(request, 'index.html' , context )

def  newDojo(request):
    if request.method == "POST":
        newdojo=Dojo.objects.create(
            name =request.POST['name'],
            city =request.POST['city'],
            state =request.POST['state'],
        )
        newdojo.save()
    return redirect ('/')

def newNinja(request):
    if request.method == 'POST':
        newNinja= Ninja.objects.create(
            first_name = request.POST['first_name'],
            last_name = request.POST['last_name'],
            dojo_id = Dojo.objects.get(id=request.POST['dojo'])
        )
        newNinja.save()

    return redirect('/')

def delete(request, _id):
    dojo = Dojo.objects.get(id=_id)
    dojo.delete()
    
    return redirect('/')