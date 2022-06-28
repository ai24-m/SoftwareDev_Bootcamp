from django.shortcuts import render, HttpResponse , redirect # add redirect to import statement

def register(request):
    return HttpResponse("placeholder for users to create a new user record")

def login(request):
    return HttpResponse("placeholder for users to log in")

def usersnew(request):
    return redirect("/register")

def user(request):
    return HttpResponse("placeholder to later display all the list of users")
