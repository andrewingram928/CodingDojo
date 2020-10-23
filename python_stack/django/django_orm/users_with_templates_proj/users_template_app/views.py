from django.shortcuts import render, redirect
from .models import Users

## RENDERING

def index(request):
    context = {
        'all_users': Users.objects.all()
    }
    return render(request, "index.html", context)

## CREATING

def add_user(request):
    if request.method == "POST":
        print(request.POST)
        Users.objects.create(first_name=request.POST['first_name'],last_name=request.POST['last_name'], email_address=request.POST['email'], age=request.POST['age'])
        return redirect('/')
    else:
        return redirect('/')

## READING
