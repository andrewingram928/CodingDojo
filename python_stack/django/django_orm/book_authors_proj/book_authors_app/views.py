from django.shortcuts import render, redirect
from .models import *

## RENDERING

def index(request):
    context = {
        'all_books' : Book.objects.all()
    }
    return render(request, 'index.html', context)

def view_authors(request):
    context = {
        'all_authors' : Author.objects.all(),
    }
    return render(request, 'view_authors.html', context)

## CREATION

def add_book(request):
    if request.method == "POST":
        Book.objects.create(title = request.POST['title'], desc = request.POST['desc'])
        return redirect('/')
    else:
        return redirect('/')

def add_book_from_instance(request):
    if request.method == "POST":
        this_book = Book.objects.get(id = request.POST['book_id'])
        this_author = Author.objects.get(id = request.POST['author_id'])
        this_book.authors.add(this_author)
        return redirect(f'/author/{this_author.id}')
    else:
        return redirect('/')

def add_author_from_instance(request):
    if request.method == "POST":
        this_book = Book.objects.get(id = request.POST['book_id'])
        this_author = Author.objects.get(id = request.POST['author'])
        this_book.authors.add(this_author)
        return redirect(f'/book/{this_book.id}')
    else:
        return redirect('/')

def add_author(request):
    if request.method == "POST":
        Author.objects.create(name= request.POST['name'], notes = request.POST['notes'])
        return redirect('/view_authors')
    else:
        return redirect('/')

## READING

def view_book(request, book_id):
    context = {
        'all_authors' : Author.objects.all(),
        'book' : Book.objects.get(id=book_id),
    }
    return render(request, 'view_book.html', context)

def view_author(request, author_id):
    context = {
        'all_books' : Book.objects.all(),
        'author' : Author.objects.get(id=author_id),
    }
    return render(request, 'view_author.html', context)
