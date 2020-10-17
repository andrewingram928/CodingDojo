from django.shortcuts import render, redirect
from django.utils.crypto import get_random_string

def landing(request):
    return render(request, "index.html")

def generate_again(request):
    request.session['ran_num'] = get_random_string(length=14)
    request.session['count'] += 1
    return redirect('/generated')

def generated(request):
    return render(request, 'generated.html')

def first_generate(request):
    request.session['ran_num'] = get_random_string(length=14)
    request.session['count'] = 1
    return redirect('/generated')

def reset(request):
    request.session['count'] = 0
    return redirect('/generated')