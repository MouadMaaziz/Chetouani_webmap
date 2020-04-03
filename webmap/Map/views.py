
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Projet, About, Pied_de_page , Message, Services, Contact_page
from Blog_app.models import Portfolio
from django.core.mail import send_mail
from django.conf import settings
from .forms import ContactForm
# Create your views here.
def home_view(request,*args,**kwargs):
    abouts= About.objects.all()
    portfolios = Portfolio.objects.all().order_by('-pk')
    contacts= Pied_de_page.objects.all()
    abouts= About.objects.all()
    services= Services.objects.all()
    #return HttpResponse("hello Grey")
    return render(request,"home.html" ,{'list':portfolios[:4],'about':abouts[0],'contact':contacts[0],'contact':contacts[0],'serv':services})

def webmap_view(request,*args,**kwargs):
    maps= Projet.objects.all()
    #return HttpResponse("hello Grey")
    return render(request,"webmap.html" ,{'proj':maps})

def base_view(request,*args,**kwargs):
    #return HttpResponse("hello Grey")
    abouts= About.objects.all()
    contacts= Pied_de_page.objects.all()
    return render(request,"base.html" ,{'about':abouts[0],'contact':contacts[0]})


def contact_view(request,*arg,**kwargs):
    if request.method == 'POST':
        name= request.POST['txtname']
        email= request.POST['txtmail']
        message= request.POST['txtmessage']
        Message.objects.create(Name= name, Email=email, message=message)

    abouts= About.objects.all()
    contacts= Pied_de_page.objects.all()
    abouts= About.objects.all()
    contenu= Contact_page.objects.all()
    return render(request,"contact.html",{'about':abouts[0],'contact':contacts[0],'contpg':contenu[0]})


def about_view(request,*arg,**kwargs):
    abouts= About.objects.all()
    contacts= Pied_de_page.objects.all()
    return render(request,"about.html",{'about':abouts[0],'contact':contacts[0]})


def assistance_view(request,*arg,**kwargs):
    return render(request,"assistance.html",{})

def topograpie_view(request,*arg,**kwargs):
    return render(request,"topograpie.html",{})

def geomatique_view(request,*arg,**kwargs):
    return render(request,"geomatique.html",{})

def formations_view(request,*arg,**kwargs):
    return render(request,"formations.html",{})
