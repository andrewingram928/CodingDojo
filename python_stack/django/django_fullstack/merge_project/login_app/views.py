from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
import bcrypt

## RENDERING

def index(request):
    return render(request, 'login_app/index.html')

def success(request):
    if 'userid' in request.session:
        context = {
            'user' : User.objects.get(id = request.session['userid'])
        }
        return render(request, 'login_app/success.html', context)
    else:
        return redirect('/login')

## CREATING

def register(request):
    if request.method == 'POST':

        errors = User.objects.validator(request.POST)

        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/login')
        else:
            password = request.POST['password']
            pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
            logged_user = User.objects.create(first_name = request.POST['first_name'], last_name = request.POST['last_name'], email = request.POST['email'], birthday = request.POST['birthday'], password = pw_hash)
            request.session['userid'] = logged_user.id
            return redirect('/login/success')
    else:
        return redirect('/login')

## ACCESSING

def login(request):
    if request.method == 'POST':

            user = User.objects.filter(email = request.POST['email'])

            if user:
                logged_user = user[0]
                if bcrypt.checkpw(request.POST['password'].encode(), logged_user.password.encode()):
                    request.session['userid'] = logged_user.id
                    return redirect('/login/success')
                else:
                    messages.error(request, 'Invalid password')
                    return redirect('/login')
            else:
                messages.error(request, 'Invalid email')
                return redirect('/login')
    else:
        return redirect('/login')

def logout(request):
    request.session.clear()
    return redirect('/login')