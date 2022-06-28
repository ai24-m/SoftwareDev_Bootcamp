from django.contrib import messages
from django.shortcuts import redirect, render
from .models import *
import bcrypt

    # Rinder the Login and Registration Page
def index(request):
    return render(request, 'index.html')


    # Render the Dashbourd Page
def dashboard(request):
    if not 'currntUser' in request.session:
        return redirect('/')
    context={
        "users" : Users.objects.get(id=request.session['currntUser']),
        "Items" : Wish.objects.all().order_by('-createdAt'),
        "granted":grantedWish.objects.all().order_by('-createdAt')
    }
    return render(request,'dashBoard.html',context)


    #Registration function accept data from the user 
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
            request.session['currntUser'] = newUser.id # named and assign session  for the user 
            return redirect('/wishes')


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
                return redirect('/wishes')
        else:
            messages.error(request, "Email does not exist!")
            return redirect('/')


    # log out function to delete the session and log out the user 
def logout(request): 
    request.session.delete()
    return redirect('/')


    #Render the Makewish Page 
def wishAdd(request):
    if not 'currntUser' in request.session:
        return redirect('/')
    context={
        "users" : Users.objects.get(id=request.session['currntUser']),

    }
    return render(request,'Makewish.html', context)

#create a new wish 
def newWish(request):
    if request.method =='POST':
        errors = Wish.objects.valdator(request.POST)
        if len(errors)>0:
            for key , value in errors.items():
                messages.error(request,value)
            return redirect('/new')
        else:
            user = Users.objects.get(id=request.session['currntUser'])
            item = request.POST['item']
            desc = request.POST['desc']
            newWish= Wish.objects.create(
                item = item,
                desc = desc ,
                createBy = user,
            ) 
            # newWish.userLikes.add(user)
            newWish.save()
        return redirect('/wishes')


def editPage(request,_id):
    if not 'currntUser' in request.session:
        return redirect('/')
    context = {
        "users": Users.objects.get(id=request.session['currntUser']),
        "wishes": Wish.objects.get(id=_id)
    }
    return render(request, 'edit.html',context)


def update(request,_id):
    if request.method == 'POST':
        wishes = Wish.objects.get(id=_id)
        errors = Wish.objects.valdator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect(f"/edit/{_id}")
        else:
            wishes.item = request.POST['item']
            wishes.desc = request.POST['desc']
            wishes.save()
            # messages.success(request, "Book successfully updated!")
            return redirect('/wishes')


def delete(request,_id):
    item = Wish.objects.get(id=_id)
    item.delete()
    return redirect("/wishes")


def state(request):
    if not 'currntUser' in request.session:
        return redirect('/')
    context={
        "users" : Users.objects.get(id=request.session['currntUser']),
        "granting":grantedWish.objects.count(),
        "userWishes": Users.objects.get(id=request.session['currntUser']).granting.count(),
        "pendingWish":Users.objects.get(id=request.session['currntUser']).itemUploader.count()

    }
    return render(request, 'state.html' ,context)


def grant(request, _id):
    if not 'currntUser' in request.session:
        redirect('/wishes')
    if request.method =='POST':
        # user = Users.objects.get(id=request.session['currntUser'])
        item = request.POST['item']
        createBy = Users.objects.get(id=request.POST['createBy'])
        createdAt =request.POST['createdAt']
        granted= grantedWish.objects.create(
            item = item,
            createdAt = createdAt,
            createBy = createBy 
        ) 
        wish=Wish.objects.get(id=_id)
        wish.delete()
        # newWish.userLikes.add(user)
        granted.save()
        return redirect('/wishes')
    return redirect('/wishes')


def like(request , _id):
        granted = grantedWish.objects.get(id=_id)
        user = Users.objects.get(id=request.session['currntUser'])
        user.likes.add(granted)
        user.save()
        return redirect('/wishes')



# def logout(request):
#     request.session.clear()
#     return redirect('/')
