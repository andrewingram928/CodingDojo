from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
from django.apps import apps

User = apps.get_model('login_app', 'User')

## RENDERING

def index(request):
    context = {
        'all_courses' : Course.objects.all()
    }
    return render(request, 'index.html', context)

## CREATING

def create(request):
    if request.method == 'POST':

        desc_errors = Description.objects.validator(request.POST)

        if len(desc_errors) > 0:
            for key, value in desc_errors.items():
                messages.error(request, value)
                return redirect('/')
        else:
            new_desc = Description.objects.create(content = request.POST['content'])

        course_errors = Course.objects.validator(request.POST)

        if len(course_errors) > 0:
            for key, value in course_errors.items():
                messages.error(request, value)
            return redirect('/')
        else:
            Course.objects.create(name = request.POST['name'], description = Description.objects.get(id = new_desc.id))
            return redirect('/')

def comment(request, course_id):
    if request.method == 'GET':
        this_course = Course.objects.get(id=course_id)
        context = {
            'course' : Course.objects.get(id=course_id),
            'all_comments' : this_course.comments.all()
        }
        return render(request, 'comment.html', context)
    else:
        Comment.objects.create(content = request.POST['content'], course = Course.objects.get(id=course_id))
        return redirect(f'/courses/comments/{course_id}')

## ADDING USER TO COURSE

def add_user(request):
    if request.method == 'POST':
        this_course = Course.objects.get(id=request.POST['course'])
        this_user = User.objects.get(id = request.POST['user'])
        this_course.user.add(this_user)
        return redirect('/courses/users_courses')
    else:
        context = {
            'all_courses' : Course.objects.all(),
            'all_users' : User.objects.all(),
        }
        return render(request, 'add_users.html', context)

## DESTROYING

def destroy(request, course_id):
    if request.method == 'GET':
        context = {
            'course' : Course.objects.get(id=course_id)
        }
        return render(request, 'destroy.html', context)
    else:
        delete = Course.objects.get(id= request.POST['course_id'])
        delete.delete()
        return redirect('/')