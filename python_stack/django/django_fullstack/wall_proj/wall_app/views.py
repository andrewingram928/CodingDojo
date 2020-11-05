from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
import bcrypt
from datetime import datetime

## RENDERING

def index(request):
    return render(request, 'index.html')

def success(request):
    if 'userid' in request.session:
        context = {
            'user' : User.objects.get(id = request.session['userid']),
            'all_messages' : Message.objects.all().order_by("-created_at"),
        }
        return render(request, 'success.html', context)
    else:
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
            logged_user = User.objects.create(first_name = request.POST['first_name'], last_name = request.POST['last_name'], email = request.POST['email'], birthday = request.POST['birthday'], password = pw_hash)
            request.session['userid'] = logged_user.id
            return redirect('/success')
    else:
        return redirect('/')

def post_message(request):
    if request.method == 'POST':
        Message.objects.create(content = request.POST['content'], user = User.objects.get(id = request.POST['user_id']))
        return redirect('/success')
    else:
        return redirect('/')

def post_comment(request):
    if request.method == 'POST':
        Comment.objects.create(content = request.POST['content'], message = Message.objects.get(id=request.POST['message_id']), user = User.objects.get(id = request.POST['user_id']))
        return redirect('/success')
    else:
        return redirect('/')

## ACCESSING

def login(request):
    if request.method == 'POST':

            user = User.objects.filter(email = request.POST['email'])

            if user:
                logged_user = user[0]
                if bcrypt.checkpw(request.POST['password'].encode(), logged_user.password.encode()):
                    request.session['userid'] = logged_user.id
                    return redirect('/success')
                else:
                    messages.error(request, 'Invalid password')
                    return redirect('/')
            else:
                messages.error(request, 'Invalid email')
                return redirect('/')
    else:
        return redirect('/')

def logout(request):
    request.session.clear()
    return redirect('/')

## DESTROYING

def delete_message(request, message_id):
    Message.objects.get(id=message_id).delete()
    # age = (this_message.created_at - datetime.now()).seconds/60
    # if age > 30:
    #     this_message.delete()
    return redirect('/success')

def delete_comment(reques, comment_id):
    Comment.objects.get(id=comment_id).delete()
    return redirect('/success')