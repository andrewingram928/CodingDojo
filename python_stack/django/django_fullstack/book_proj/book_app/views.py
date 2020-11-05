from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
import bcrypt

## RENDERING

def index(request):
    return render(request, 'index.html')

def books(request):
    if 'user_id' in request.session:
        context = {
            'user' : User.objects.get(id = request.session['user_id']),
            'all_books' : Book.objects.all(),
        }
        return render(request, 'books.html', context)
    else:
        return redirect('/')

def logout(request):
    request.session.clear()
    return redirect('/')

## CREATING

def register(request):
    if request.method == 'POST':

        errors = User.objects.validator(request.POST)

        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/')
        else:
            password = request.POST['password']
            pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
            logged_user = User.objects.create(first_name = request.POST['first_name'], last_name = request.POST['last_name'], email = request.POST['email'], password = pw_hash)
            request.session['user_id'] = logged_user.id
            return redirect('/books')
    else:
        return redirect('/')

def add_book(request):
    if request.method == 'POST':
        this_book = Book.objects.create(title = request.POST['title'], desc = request.POST['desc'],uploaded_by = User.objects.get(id=request.POST['user_id']))
        this_book.users_who_like.add(User.objects.get(id=request.POST['user_id']))
        return redirect('/books')
    else:
        return redirect('/books')

def favorite_book(request, book_id):
    this_user = User.objects.get(id = request.session['user_id'])
    this_book = Book.objects.get(id=book_id)
    if this_user in this_book.users_who_like.all():
        this_book.users_who_like.remove(this_user)
        return redirect('/books')
    this_book.users_who_like.add(this_user)
    return redirect('/books')

## ACCESSING

def login(request):
    if request.method == 'POST':

            user = User.objects.filter(email = request.POST['email'])

            if user:
                logged_user = user[0]
                if bcrypt.checkpw(request.POST['password'].encode(), logged_user.password.encode()):
                    request.session['user_id'] = logged_user.id
                    return redirect('/books')
                else:
                    messages.error(request, 'Invalid password')
                    return redirect('/')
            else:
                messages.error(request, 'Invalid email')
                return redirect('/')
    else:
        return redirect('/')

## READING/UPDATING

def one_book(request, book_id):
    if request.method == 'GET':
        if 'user_id' in request.session:
            context = {
                'user' : User.objects.get(id = request.session['user_id']),
                'this_book' : Book.objects.get(id = book_id),
        }
            return render(request, 'one_book.html', context)
        else:
            return redirect('/')
    if request.method == 'POST':
        this_user = User.objects.get(id = request.session['user_id'])
        this_book = Book.objects.get(id=book_id)
        if this_user == this_book.uploaded_by:
            this_book.title = request.POST['title']
            this_book.desc = request.POST['desc']
            this_book.save()
            return redirect('/books')
        else:
            return redirect('/')

def my_favorites(request):
    if 'user_id' in request.session:
        context = {
            'user' : User.objects.get(id=request.session['user_id'])
        }
        return render(request, 'my_favorites.html', context)
    return redirect('/')

## DELETION

def delete_book(request, book_id):
    if request.method == 'POST':
        this_user = User.objects.get(id = request.session['user_id'])
        this_book = Book.objects.get(id=book_id)
        if this_user == this_book.uploaded_by:
            this_book.delete()
        return redirect('/books')
    return redirect('/')
