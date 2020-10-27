from django.shortcuts import render, redirect
from .models import Ninja, Dojo

## RENDERING

def index(request):
    context = {
        'all_dojos': Dojo.objects.all(),
        'all_ninjas': Ninja.objects.all()
    }
    return render(request, 'index.html', context)

## CREATING

def add_dojo(request):
    if request.method == 'POST':
        print(request.POST)
        Dojo.objects.create(name = request.POST['name'], city = request.POST['city'], state = request.POST['state'])
        return redirect('/')
    else:
        return redirect('/')

def add_ninja(request):
    if request.method == 'POST':
        print(request.POST)
        Ninja.objects.create(first_name = request.POST['first_name'], last_name = request.POST['last_name'], dojo = Dojo.objects.get(id=request.POST['dojo']))
        return redirect('/')
    else:
        return redirect('/')