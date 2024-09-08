from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Places, News, Demandes, Immigres, Documents, Sejours
import os
from dgm_site import settings
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import pdfkit
from django.template.loader import get_template

# Create your views here.

def home(request):
    places = Places.objects.all().order_by('-id')[:3]
    news = News.objects.all().order_by('-id')[:3]
    na = news[0]
    nb = news[1]
    nc = news[2]
    return render(request, 'index.html', context={'places':places, 'news':news, 'na':na, 'nb':nb, 'nc':nc})

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
    places = Places.objects.all().order_by('-id')
    return render(request, 'dgm_app/more.html', context={'places':places})

def one(request, id):
    one = Places.objects.get(id=id)
    return render(request, 'dgm_app/one.html', context={'one':one})

def form_demanede(request):
    if request.method == 'POST':
        nom = request.POST['nom']
        prenom = request.POST['prenom']
        postnom = request.POST['postnom']
        sexe = request.POST['sexe']
        date_nais = request.POST['date_nais']
        nationalite = request.POST['nationalite']
        pays_res = request.POST['pays_res']
        address_res = request.POST['address_res']
        profession = request.POST['profession']
        provenance = request.POST['provenance']
        img = request.FILES['img']

        num_visa = request.POST['num_visa']
        num_carte_id = request.POST['num_carte_id']

        but_sej = request.POST['but_sej']
        debut_sej = request.POST['debut_sej']
        fin_sej = request.POST['fin_sej']
        ville = request.POST['ville']

        with open(os.path.join(settings.MEDIA_ROOT, img.name),'wb') as file:
            for chunk in img.chunks():
                img.write(chunk)

        immigre = Immigres(nom=nom, postnom=postnom, prenom=prenom, sexe=sexe, date_nais=date_nais, 
                           nationalite=nationalite, pays_residence=pays_res, adress_residence=address_res, profession=profession, 
                           provenance=provenance, img=img)
        immigre.save()
        
        document = Documents(num_visa=num_visa, num_carte_id=num_carte_id)
        document.save()

        sejour = Sejours(but = but_sej, date_debut=debut_sej, date_fin=fin_sej, ville=ville)
        sejour.save()

        demande = Demandes(immigre=immigre, document=document, sejour=sejour)
        demande.save()

    return render(request, 'dgm_app/form_demande.html')

def dashboard(request):
    nb_user = len(User.objects.all())
    nb_new = len(News.objects.all())
    nb_place = len(Places.objects.all())
    nb_lu = len(Demandes.objects.filter(lu=False))

    return render(request, 'dgm_app/dashboard.html', context={'nb_user':nb_user, 'nb_new':nb_new, 'nb_place':nb_place, 'nb_lu':nb_lu})

def gst_user(request):
    users = User.objects.all()
    return render(request, 'dgm_app/gst_user.html', context={'users':users})

def gst_new(request):
    news = News.objects.all()
    return render(request, 'dgm_app/gst_new.html', context={'news':news})

def add_new(request):
    if request.method == 'POST':
        titre = request.POST['titre'] 
        img = request.FILES['img'] 
        desc = request.POST['desc'] 

        with open(os.path.join(settings.MEDIA_ROOT, img.name),'wb') as file:
            for chunk in img.chunks():
                img.write(chunk)

        new = News(titre=titre, img=img, description=desc)
        new.save()

        return redirect ('gst_new')

    return render(request, 'dgm_app/add_new.html')

def delete_new(request, id):
    new = News.objects.get(id=id)
    new.delete()

    return redirect ('gst_new')

def gst_place(request):
    places = Places.objects.all()
    return render(request, 'dgm_app/gst_place.html', context={'places':places})

def add_place(request):
    if request.method == 'POST':
        nom = request.POST['nom'] 
        img = request.FILES['img'] 
        desc = request.POST['desc'] 

        with open(os.path.join(settings.MEDIA_ROOT, img.name),'wb') as file:
            for chunk in img.chunks():
                img.write(chunk)

        new = Places(nom=nom, img=img, description=desc)
        new.save()

        print('Je suis là')

        return redirect ('gst_place')
    return render(request, 'dgm_app/add_place.html')

def delete_place(request, id):
    place = Places.objects.get(id=id)
    place.delete()

    return redirect ('gst_place')

def gst_demande(request):
    demandes = Demandes.objects.all().order_by('-id')
    for demande in demandes:
        demande.lu = True
        demande.save()

    default_page = 1

    page = request.GET.get('page', default_page)

    items_per_page = 5

    paginator = Paginator(demandes, items_per_page)

    try:
        items_page = paginator.page(page)
    except PageNotAnInteger:
        items_page = paginator.page(default_page)
    except EmptyPage:
        items_page = paginator.page(paginator.num_pages)

    demandes = items_page

    return render(request, 'dgm_app/gst_demande.html', context={'demandes':demandes})

def demande_a(request, id):
    demande = Demandes.objects.get(id=id)
    demande.avis = 'A'
    demande.save()

    return redirect('gst_demande')

def demande_n(request, id):
    demande = Demandes.objects.get(id=id)
    demande.avis = 'D'
    demande.save()

    return redirect('gst_demande')


def detail(request, id):
    demande = Demandes.objects.get(id=id)
    return render(request, 'dgm_app/detail_info.html', context={'demande':demande})

def get_result(request, id):
    demandes = Demandes.objects.get(id=id)
    context = {'demandes':demandes}

    template = get_template('dgm_app/etat_sortie.html')

    html = template.render(context)

    option = {
        'page-size': 'Letter',
        'encoding': 'UTF-8',
        'enable-local-file-access': ""
    }

    pdf = pdfkit.from_string(html, False, option)

    response = HttpResponse(pdf, content_type='application/pdf')
    response['Content-Disposition'] = 'attachement'

    return response
