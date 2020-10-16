from django.shortcuts import render, redirect

def index(request):
    return render(request, 'index.html')

def assign(request):
    if request.method == 'POST':
        print(request.POST)
        request.session['name'] = request.POST['name']
        request.session['language'] = request.POST['language']
        request.session['location'] = request.POST['location']
        request.session['comment'] = request.POST['comment']
        return redirect('/result')
    else:
        return render(request, 'index.html')

def result(request):
    return render(request, 'result.html')