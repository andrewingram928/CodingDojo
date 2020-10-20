from django.shortcuts import render, redirect
import random

def landing(request):
    return render(request, "index.html")

def process(request):
    if request.method == "POST":
        request.session['count'] += 1
        if request.POST['hidden'] == 'farm':
            request.session['gold'] += random.randint(10,20)
            return redirect('/')
        if request.POST['hidden'] == 'cave':
            request.session['gold'] += random.randint(5,10)
            return redirect('/')
        if request.POST['hidden'] == 'house':
            request.session['gold'] += random.randint(2,5)
            return redirect('/')
        if request.POST['hidden'] == 'casino':
            request.session['gold'] += random.randint(-50,50)
            return redirect('/')
        if request.session['count'] == request.session['turn_limit']:
            return redirect('/game_complete')
        if request.session['gold'] >= request.session['gold_goal']:
            return redirect('/game_complete')
def rules(request):
    if request.method == "POST":
        request.session['gold_goal'] = request.POST['gold_goal']
        request.session['turn_limit'] = request.POST['turn_limit']
        return redirect('/')

def complete(request):
    return render(request, "game_complete.html")