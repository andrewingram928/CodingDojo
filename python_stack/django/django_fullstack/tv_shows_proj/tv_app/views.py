from django.shortcuts import render, redirect
from .models import *
from datetime import datetime
from django.contrib import messages

## RENDERING

def index(request):
    return redirect('/shows')

## READING

def shows(request):
    context = {
        'all_shows' : Show.objects.all()
    }
    return render(request, 'all_tv_shows.html', context)

def one_show(request, show_id):
    context = {
        'show' : Show.objects.get(id = show_id)
    }
    return render(request, 'one_tv_show.html', context)

def one_network(request, network_id):
    context = {
        'network' : Network.objects.get(id = network_id)
    }
    return render(request, 'one_network.html', context)

## CREATING

def create_show(request):
    if request.method == 'POST':

        errors = Show.objects.basic_validator(request.POST)

        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/shows/create')
        else:
            new_show = Show.objects.create(title = request.POST['title'], release_date = request.POST['release_date'], network = Network.objects.get(id=request.POST['network']), desc = request.POST['desc'])
            return redirect(f'/shows/{new_show.id}')
    else:
        context = {
            'all_networks' : Network.objects.all()
        }
        return render(request, 'create_show.html', context)

def create_network(request):
    if request.method == 'POST':
        new_network = Network.objects.create(name = request.POST['name'])
        return redirect(f'/networks/{new_network.id}')
    else:
        return render(request, 'create_network.html')

## UPDATING

def edit_show(request, show_id):
    if request.method == 'POST':
        show = Show.objects.get(id= show_id)
        errors = Show.objects.basic_validator(request.POST)

        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect(f'/shows/{show.id}/edit')
        else:
            show.title =  request.POST['title']
            show.release_date = request.POST['release_date']
            show.network = Network.objects.get(id=request.POST['network'])
            show.desc = request.POST['desc']
            show.save()
            return redirect(f'/shows/{show.id}')
    else:
        this_show = Show.objects.get(id=show_id)
        context = {
            'show' : Show.objects.get(id=show_id),
            'all_networks' : Network.objects.all(),
            'date' : datetime.strftime(this_show.release_date, '%Y-%m-%d')
        }
        return render(request, 'edit_show.html', context)

def edit_network(request, network_id):
    if request.method == 'POST':
        network = Network.objects.get(id= network_id)
        network.name =  request.POST['name']
        network.save()
        return redirect(f'/networks/{network.id}')
    else:
        context = {
            'network' : Network.objects.get(id=network_id),
        }
        return render(request, 'edit_network.html', context)

## DESTROYING

def destroy(request, show_id):
    show = Show.objects.get(id=show_id)
    show.delete()
    return redirect('/shows')