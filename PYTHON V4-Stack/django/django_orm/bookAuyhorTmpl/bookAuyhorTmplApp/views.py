from django.shortcuts import render, redirect
from .models import *



def index(request):
    context={
        'books':Book.objects.all(),
    }
    return render(request,'addBooks.html', context)



def addBook(request):
    if request.method=='POST':
        _newBook= Book.objects.create(
            title=request.POST['title'],
            desc=request.POST['desc'],
        )
        _newBook.save()
    return redirect('/')



def InfoBook(request, _id):
    context={
        'book':Book.objects.get(id=_id),
        'authors':Author.objects.all()
    } 
    return render(request,'BookInfo.html',context)


def delete(request, _idBook):
    book = Book.objects.get(id=_idBook)
    book.delete()
    return redirect('/')

# Add Author To Book
def addAuthor_Book(request, _id):
    _thisBook=Book.objects.get(id=_id)
    _thisAuthor=Author.objects.get(id=request.POST['author_id'])
    _thisBook.authors.add(_thisAuthor)

    return redirect(f"/books/{_id}")

# page of author
def author(request):
    context={
        'authors':Author.objects.all()
    }
    return render(request, 'addAuthor.html', context)

# Add a new author AND see a table of authors in page(Add author)
def addAuthor(request):
    if request.method=='POST':
        _newAuthor=Author.objects.create(
            fname=request.POST['fname'],
            lname=request.POST['lname'],
            notes=request.POST['notes'],
        )
        _newAuthor.save()
        return redirect('/authors')

# View Author
def InfoAuthor(request, _id):
    _author=Author.objects.get(id=_id)
    context={
        'books':Book.objects.all(),
        'author':_author,
    } 
    return render(request,'AuthorInfo.html',context)

# Delete author by ID
def delete_author(request, _idAuthor):
    author = Author.objects.get(id=_idAuthor)
    author.delete()
    return redirect('/authors')

# Add Book To Author
def addBook_Author(request, _id):
    _thisAuthor=Author.objects.get(id=_id)
    _thisBook=Book.objects.get(id=request.POST['book_id'])
    _thisAuthor.books.add(_thisBook)
    
    return redirect(f"/authors/{_id}")