from django.contrib import messages
from django.shortcuts import redirect, render
from .models import *
import bcrypt

    # Rinder the Login and Registration Page
def index(request):
    return render(request, 'index.html')


def register(request):
    if request.method =='POST': #to check if the form method post or get 

        errors = Users.objects.validator(request.POST) # define a variable to access to the validator class 
        if len(errors)>0:
            for key ,value in errors.items():
                messages.error(request, value)
            return redirect('/')
        else:
            _fname = request.POST['fname'] #accept the data from the user throu '' 
            _lname = request.POST['lname']
            _email = request.POST['email']
            _password = request.POST['password']
            pwHash = bcrypt.hashpw(_password.encode(), bcrypt.gensalt()).decode() #hashing the password 
            newUser =Users.objects.create(
                fname=_fname,
                lname=_lname,
                email =_email,
                password= pwHash
                ) # create new data for the user
            newUser.save() # save the data
            # messages.success(request," successfully Registered!")
            request.session['currntUser'] = newUser.id # named and assign session  for the user 
            return redirect('/success')

def login(request):
    if request.method=='POST':
        users = Users.objects.filter(email=request.POST['email']) # filtering emails  and make sure its exist inside the data
        if not request.POST['email']:
            messages.error(request,"The email field is required !")
            # return redirect('/')
        if not request.POST['password']:
            messages.error(request,"The Password field is required !")
            return redirect('/')
        elif len(users)==1: 
            if not bcrypt.checkpw(request.POST['password'].encode(),users[0].password.encode()):
                messages.error(request, "Email or Password is incorrect!")
                return redirect('/')
            else:
                request.session['currntUser'] = users[0].id
                return redirect('/success')
        else:
            messages.error(request, "Email does not exist!")
            return redirect('/')

def success(request):
    if 'currntUser' not in request.session:
        return redirect('/')
    context = {
        'user': Users.objects.get(id=request.session['currntUser'])
    }
    return render(request,'success.html',context)


    # log out function to delete the session and log out the user 
def logout(request): 
    request.session.delete()
    return redirect('/')


