
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Webmap, About, Pied_de_page , Message, Prestations_page, Contact_page, Tete_de_page, Accueil_page, Partenairs, Menu_bar
from Blog_app.models import Portfolio
from django.core.mail import send_mail
from django.conf import settings
from .forms import ContactForm
# Create your views here.
def home_view(request,*args,**kwargs):

    portfolios = Portfolio.objects.all().order_by('-pk')
    contacts= Pied_de_page.objects.all()
    abouts= About.objects.all()
    services= Prestations_page.objects.all()
    tete=Tete_de_page.objects.all()
    Accueil=Accueil_page.objects.all()
    Menu=Menu_bar.objects.all()
    #return HttpResponse("hello Grey")
    return render(request,"home.html" ,{'list':portfolios[:4],'about':abouts[0],'contact':contacts[0],'serv':services,'tete':tete[0],'Accueil':Accueil[0],'menu':Menu[0]})

def webmap_view(request,*args,**kwargs):
    maps= Webmap.objects.all()
    #return HttpResponse("hello Grey")
    return render(request,"webmap.html" ,{'proj':maps})

def base_view(request,*args,**kwargs):
    #return HttpResponse("hello Grey")
    abouts= About.objects.all()
    contacts= Pied_de_page.objects.all()
    tete=Tete_de_page.objects.all()
    Menu=Menu_bar.objects.all()
    return render(request,"base.html" ,{'about':abouts[0],'contact':contacts[0],'tete':tete[0],'menu':Menu[0]})


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
    tete=Tete_de_page.objects.all()
    Menu=Menu_bar.objects.all()
    return render(request,"contact.html",{'about':abouts[0],'contact':contacts[0],'contpg':contenu[0],'tete':tete[0],'menu':Menu[0]})


def about_view(request,*arg,**kwargs):
    portfolios = Portfolio.objects.all().order_by('-pk')
    abouts= About.objects.all()
    contacts= Pied_de_page.objects.all()
    services= Prestations_page.objects.all()
    tete=Tete_de_page.objects.all()
    part= Partenairs.objects.all()
    Menu=Menu_bar.objects.all()
    return render(request,"about.html",{'about':abouts[0],'contact':contacts[0],'tete':tete[0],'list':portfolios[:4],'serv':services, 'part':part,'menu':Menu[0]})


def prestations_view(request,prestation_id):
    detailpres= get_object_or_404(Prestations_page, pk=prestation_id)
    services= Prestations_page.objects.all()
    tete=Tete_de_page.objects.all()
    contacts= Pied_de_page.objects.all()
    abouts= About.objects.all()
    Menu=Menu_bar.objects.all()
    services= Prestations_page.objects.all()
    Accueil=Accueil_page.objects.all()
    return render(request,"prestations.html",{'presdet':detailpres, 'contact':contacts[0],'tete':tete[0],'about':abouts[0],'menu':Menu[0],'serv':services,'Accueil':Accueil[0]})
