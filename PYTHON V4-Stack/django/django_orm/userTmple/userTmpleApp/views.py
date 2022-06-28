from multiprocessing import context
from django.shortcuts import render, HttpResponse , redirect
from .models import *


def index(request):
    users = Users.objects.all()
    context={
        'users' : users
    }
    return render(request,'index.html', context)

def newUser(request):
    if request.method =='POST':
        newUser = Users.objects.create(
            fname = request.POST['fname'],
            lname = request.POST['lname'],
            email =request.POST['email'],
            age =request.POST['age']
        )
        newUser.save()
    return redirect('/')