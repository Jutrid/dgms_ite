from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Places, News

# Create your views here.

def home(request):
    places = Places.objects.all().order_by('-id')[:3]
    a = places[0]
    b = places[1]
    c = places[2]
    news = News.objects.all().order_by('-id')[:3]
    na = news[0]
    nb = news[1]
    nc = news[2]
    return render(request, 'index.html', context={'a':a, 'b':b, 'c':c, 'news':news, 'na':na, 'nb':nb, 'nc':nc})

def logIn(request):
    if request.method == 'POST':
        username = request.POST['username']
        pwd = request.POST['password'] 

        my_user = authenticate(username=username, password=pwd)

        if my_user is not None:
            login(request, my_user)
            return redirect('home')
        else:
            messages.error(request, 'Le mot de passe ou le nom d\'utilisateur est incorrect')
            return redirect('login')
        
    return render(request, 'login.html')

def signIn(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password1 = request.POST['password1']

        if User.objects.filter(username=username):
            messages.error(request, 'Ce nom d\'utilisateur existe déja')
            return redirect('signin')

        if User.objects.filter(email=email):
            messages.error(request, 'Ce email est déja enregistré')
            return redirect('signin')

        if User.objects.filter(username=username):
            messages.error(request, 'Ce compte email est déjà utilisé')
            return redirect('signin')

        if len(password) < 8:
            messages.error(request, 'Les mots de passe doit avoir au moins 8 caractères')
            return redirect('signin')

        if password != password1:
            messages.error(request, 'Les mots de passe ne sont pas identiques')
            return redirect('signin')
        
        if not password.isalnum():
            messages.error(request, 'Le mot de passe doit pas que contenir des chiffres et des lettre')
            return redirect('signin')
        
        u = User.objects.create_user(username=username, email=email, password=password)
        u.save()

        return redirect('login')
    
    return render(request, 'signin.html')

def more(request):
    places = Places.objects.all()
    return render(request, 'dgm_app/more.html', context={'places':places})

def one(request, id):
    one = Places.objects.get(id=id)
    return render(request, 'dgm_app/one.html', context={'one':one})

def form_demanede(request):
    return render(request, 'dgm_app/form_demande.html')

def dashboard(request):
    nb_user = len(User.objects.all())
    nb_new = len(News.objects.all())
    nb_place = len(Places.objects.all())
    return render(request, 'dgm_app/dashboard.html', context={'nb_user':nb_user, 'nb_new':nb_new, 'nb_place':nb_place})

def gst_user(request):
    users = User.objects.all()
    return render(request, 'dgm_app/gst_user.html', context={'users':users})

def gst_new(request):
    news = News.objects.all()
    return render(request, 'dgm_app/gst_new.html', context={'news':news})

def add_place(request):
    return render(request, 'dgm_app/add_place.html')

def gst_place(request):
    places = Places.objects.all()
    return render(request, 'dgm_app/gst_new.html', context={'news':places})

