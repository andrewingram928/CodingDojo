from django.shortcuts import render, redirect
import random

def landing(request):
    if 'gold' in request.session:
        pass
    else:
        request.session['gold'] = 0
    if 'count' in request.session:
        pass
    else:
        request.session['count'] = 0
    if 'gold_goal' in request.session:
        pass
    else:
       request.session['gold_goal'] = None
    if 'turn_limit' in request.session:
        pass
    else:
        request.session['turn_limit'] = None
    return render(request, "index.html")

def process(request):
    if request.method == "POST":
        def check():
            if request.session['gold'] >= int(request.session['gold_goal']) or request.session['count'] >= int(request.session['turn_limit']):
                print(request.session['gold'])
                print(request.session['gold_goal'])
                return redirect('/game_complete')
        request.session['count'] += 1
        if request.POST['hidden'] == 'farm':
            request.session['gold'] += random.randint(10,20)
            check()
            return redirect('/')
        if request.POST['hidden'] == 'cave':
            request.session['gold'] += random.randint(5,10)
            check()
            return redirect('/')
        if request.POST['hidden'] == 'house':
            request.session['gold'] += random.randint(2,5)
            check()
            return redirect('/')
        if request.POST['hidden'] == 'casino':
            request.session['gold'] += random.randint(-50,50)
            check()
            return redirect('/')

def rules(request):
    if request.method == "POST":
        request.session['gold_goal'] = request.POST['gold_goal']
        request.session['turn_limit'] = request.POST['turn_limit']
        return redirect('/')

def complete(request):
    return render(request, "game_complete.html")

def reset(request):
    request.session.clear()
    return redirect('/')