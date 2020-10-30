from django.shortcuts import render, redirect
from .models import *
from datetime import datetime

## RENDERING

def index(request):
    return redirect('/shows')

def create_show(request):
    context = {
        'all_networks' : Network.objects.all()
    }
    return render(request, 'create_show.html', context)

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

def edit_show(request, show_id):
    this_show = Show.objects.get(id=show_id)
    context = {
        'show' : Show.objects.get(id=show_id),
        'all_networks' : Network.objects.all(),
        'date' : datetime.strftime(this_show.release_date, '%Y-%m-%d')
    }
    return render(request, 'edit_show.html', context)

## CREATING

def create_show_process(request):
    if request.method == 'POST':
       new_show = Show.objects.create(title = request.POST['title'], release_date = request.POST['release_date'], network = Network.objects.get(id=request.POST['network']), desc = request.POST['desc'])
       return redirect(f'/shows/{new_show.id}')
    return redirect('/')

## UPDATING

def edit_show_process(request, show_id):
    if request.method == 'POST':
        show = Show.objects.get(id= show_id)
        show.title =  request.POST['title']
        if request.POST['release_date'] == "":
            pass
        else:
            if request.POST['release_date'] != show.release_date:
                show.release_date = request.POST['release_date']
        show.network = Network.objects.get(id=request.POST['network'])
        show.desc = request.POST['desc']
        show.save()
        return redirect(f'/shows/{show.id}')
    return redirect('/')

## DESTROYING

def destroy(request, show_id):
    show = Show.objects.get(id=show_id)
    show.delete()
    return redirect('/shows')