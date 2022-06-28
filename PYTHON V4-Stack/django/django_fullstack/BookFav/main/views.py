from multiprocessing import context
from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .models import *
import bcrypt


def index(request):
    return render(request, 'index.html')


def register(request):
    if request.method =='POST':
        errors = Users.objects.validator(request.POST)
        if len(errors)>0:
            for key ,value in errors.items():
                messages.error(request, value)
            return redirect('/')
        else:
            _fname = request.POST['fname']
            _lname = request.POST['lname']
            _email = request.POST['email']
            _password = request.POST['password']
            pwHash = bcrypt.hashpw(_password.encode(), bcrypt.gensalt()).decode()
            newUser =Users.objects.create(
                fname=_fname,lname=_lname,email =_email,password= pwHash
                )
            newUser.save()
            request.session['currntUser'] = newUser.id
            return redirect('/books')

def login(request):
    if request.method=='POST':
        users = Users.objects.filter(email=request.POST['email'])
        if len(users)==1:
            if not bcrypt.checkpw(request.POST['password'].encode(),users[0].password.encode()):
                messages.error(request, "Email or Password is incorrect!")
                return redirect('/')
            else:
                request.session['currntUser'] = users[0].id
                return redirect('/books')
        else:
            messages.error(request, "Email does not exist!")
            return redirect('/')


def books(request):
    if not 'currntUser' in request.session:
        return redirect('/')
    context={
        "user" : Users.objects.get(id=request.session['currntUser']),
        "books" : Books.objects.all().order_by('-createdAt'),
    }
    return render(request,'AddBooks.html',context )


def newBook(request):
    if request.method =='POST':
        errors = Books.objects.valdator(request.POST)
        if len(errors)>0:
            for key , value in errors.items():
                messages.error(request,value)
                return redirect('/books')
        else:
            user = Users.objects.get(id=request.session['currntUser'])
            title = request.POST['title']
            desc = request.POST['desc']
            newBook= Books.objects.create(
                title = title,
                desc = desc ,
                uplodedBy = user,
            ) 
            newBook.userLikes.add(user)
            newBook.save()
            return redirect('/books')

def bookPage(request, _id):
    if not 'currntUser' in request.session:
        return redirect('/')
    context = {
        "user": Users.objects.get(id=request.session['currntUser']),
        "book": Books.objects.get(id=_id)
    }
    return render(request, 'Bookdetails.html', context)

def bookLiked(request, _id):
    book = Books.objects.get(id=_id)
    user = Users.objects.get(id=request.session['currntUser'])
    book.userLikes.add(user)
    book.save()
    return redirect(request.META.get('HTTP_REFERER'))

def unlikeBook(request, _id):
    user=request.session['currntUser']
    book=Books.objects.get(id=_id)
    this_user=Users.objects.get(id=user)
    book.userLikes.remove(this_user)
    return redirect (request.META.get('HTTP_REFERER'))

def deleteBook(request, _id):
    book = Books.objects.get(id=_id)
    if book.uplodedBy.id == request.session['currntUser']:
        book.delete()
    return redirect('/books')

def update(request,_id):
    if request.method == 'POST':
        book = Books.objects.get(id=_id)
        errors = Books.objects.valdator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect(f"/books/{_id}")
        else:
            book.title = request.POST['title']
            book.desc = request.POST['desc']
            book.save()

            messages.success(request, "Book successfully updated!")
            return redirect(f'/books/{_id}')

# def profile(request, _id):
#     context={
#         "user":Users.objects.get(id=_id),
#         'reviewBook' :Books.objects.get(id=request.session['currntUser']),
#     }
#     return render(request,'profile.html',context)


def logout(request):
    request.session.delete()
    return redirect('/')
