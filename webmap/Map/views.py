
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Webmap, About, Pied_de_page , Message, Prestations_page, Contact_page, Tete_de_page, Accueil_page, Partenairs, Menu_bar, Intro_prestation
from Blog_app.models import Portfolio
from django.core.mail import send_mail
from django.conf import settings
from .forms import ContactForm
import folium
import numpy as np
import geopandas
import branca
from folium import plugins
from folium.plugins import MousePosition, Draw, MeasureControl, Search
# Create your views here.
def home_view(request,*args,**kwargs):

    portfolios = Portfolio.objects.all().order_by('-pk')
    contacts= Pied_de_page.objects.all()
    abouts= About.objects.all()
    services= Prestations_page.objects.all()
    tete=Tete_de_page.objects.all()
    Accueil=Accueil_page.objects.all()
    Menu=Menu_bar.objects.all()
    contenu= Contact_page.objects.all()
    #return HttpResponse("hello Grey")
    return render(request,"home.html" ,{'list':portfolios[:4],'about':abouts[0],'contact':contacts[0],'serv':services,'tete':tete[0],'Accueil':Accueil[0],'menu':Menu[0],'contpg':contenu[0]})

def webmap_view(request,*args,**kwargs):
    maps= Webmap.objects.all()
    #return HttpResponse("hello Grey")
    return render(request,"webmap.html" ,{'proj':maps})

def folium_view(request,*args,**kwargs):

    #================================================== Model data================================================
    data= Webmap.object.all()[:50]
    m = folium.Map([29,-8.86],tiles='OpenStreetMap' , zoom_start=5)
    html_string = m.get_root().render()
    test = folium.Html('<b>Hello world</b>', script=True)
    media_url = settings.MEDIA_ROOT
    #================================================External data json,gejson ...=======================================
    #jsondata= './webmap/static/communes.geojson'
    #commun=geopandas.read_file(jsondata)


    # ====================================================================Plugins===============================================
    #More Tiles
    folium.TileLayer('Stamen Watercolor').add_to(m)
    plugins.Fullscreen(position='bottomright',title='Expand me',title_cancel='Exit me',force_separate_button=True).add_to(m)
    #plugins.Geocoder().add_to(m)
    plugins.LocateControl(auto_start=False).add_to(m)

    #Measure control
    m.add_child(MeasureControl(position='topleft'))
    # Showing coordinates
    formatter = "function(num) {return L.Util.formatNum(num, 3) + ' º ';};"
    MousePosition(
    position='topright',
    separator=' | ',
    empty_string='NaN',
    lng_first=True,
    num_digits=20,
    prefix='Coordinates:',
    lat_formatter=formatter,
    lng_formatter=formatter,
    ).add_to(m)
    ###################################################################################################################################################################################################

    #############################################################################################################################################################################################
    #============================================================LayerGroups names
    fg = folium.FeatureGroup(name='All groups')
    m.add_child(fg)
    g1 = plugins.FeatureGroupSubGroup(fg, 'Group1')
    m.add_child(g1)
    g2 = plugins.FeatureGroupSubGroup(fg, 'Group2')
    m.add_child(g2)
    #------------ external data group json, geojson ...
    #extdata = plugins.FeatureGroupSubGroup(fg, 'communes',show=False)
    #m.add_child(extdata)

    # ===========================================================filtering using data ===========================================================================================================
    for y in data:
        grpopup = "<div class = popupdiv><img class='popupimg' src ="+ y.link + '>'+"<br><p class='strong'>"+y.Nom+"</p>"+"<p class='desc'>"+ y.Services + "</p></div>" +"<div class= ''>"+ y.Description_si_disop + '</div> <br>'+"<span class='fas fa-map-pin'></span> "+ y.Adress + '<br>'+"<div class= 'telpop'>"+ y.Tel + '</div><br>'
        grimgurl= media_url +'/'+ y.img.name
        grcustomIcon = folium.features.CustomIcon(grimgurl, icon_size=(30,30))
        #-----------------------------------------Criterea 1 ---------------------------------------------------------
        if y.Nom == 'jarouub':
            folium.Marker(location=[y.geom.y, y.geom.x], popup= grpopup,radius=40, icon=grcustomIcon).add_to(g1)

        #-----------------------------------------Criterea 2 -------------------------------------------------------------
        elif  y.Nom == 'lol':
            folium.Marker(location=[y.geom.y, y.geom.x], popup= grpopup,radius=40, icon=grcustomIcon).add_to(g2)

        #-------------------------For object that meet none of the Criterea ----------------------------------------------
        else:
            folium.Marker(location=[y.geom.y, y.geom.x], popup= grpopup,radius=40, icon=grcustomIcon ).add_to(fg)

        #--------------------------External data group -----------------------------------------------------------------

        #folium.GeoJson(commun,name='communes',overlay=False).add_to(extdata)

    folium.LayerControl(collapsed=True).add_to(m)


    #==============================================================This to add element inside the template generated by Folium ====================================================================

    style_statement = '''<style>    .leaflet-control{color:#f9f9f9; background-color:#000c } .leaflet-popup-content {margin: auto auto 10% auto;line-height: 1.4;text-align: center;} .popupimg{width:100%;margin-left:0px} .leaflet-popup-content-wrapper {width: 200px;text-align: center;}.leaflet-container {  /* all maps */height: 600px;width: 90%;margin: auto;z-index: 0;}@media(max-width:750px){.leaflet-container{height:500px;width:94%;}}#specialbigmap{height:800px;}/*Resizethe'display_raw'textbox*/.django-leaflet-raw-textarea{width:100%;}.bd-placeholder-img{font-size:1.125rem;text-anchor:middle;-webkit-user-select:none;-moz-user-select:none;-ms-user-select:none;user-select:none;}@media(min-width:768px){.bd-placeholder-img-lg{font-size:3.5rem;}}.leaflet-container .leaflet-marker-pane img{max-width:none!important;max-height:none!important;border-radius:100%;border-style:double;border-width:0.4rem; border-color:#000}.leaflet-touch .leaflet-control-layers, .leaflet-touch .leaflet-bar{border:1pxsolidrgb(128,128,128);background-clip:padding-box;}.leaflet-popup-content-wrapper, .leaflet-popup-tip{background:#000000e8;color:#9aa3a6;box-shadow:03px14pxrgba(0,0,0,0.9);border-radius:1%;}.leaflet-popup-content{margin:5px19px1px19px;line-height:1.2;} .telpop{font-weight:bold}.servicespop{font-size:1.15rem;font-weight:bold;}.fas{margin-right:3%;color:#096cb1;font-size:medium;}.nompop{font-size:18px;position:relative;}.description{text-align:center;position:static;text-transform:uppercase;}.label{color:#096cb1;font-size:14px;font-family:'Roboto';}.leaflet-container{/*allmaps*/height:600px;width:90%;margin:auto;z-index:0;}@media(max-width:750px){.leaflet-container{height:500px;width:94%;}}#specialbigmap{height:800px;}/*Resizethe'display_raw'textbox*/.django-leaflet-raw-textarea{width:100%;}.bd-placeholder-img{font-size:1.125rem;text-anchor:middle;-webkit-user-select:none;-moz-user-select:none;-ms-user-select:none;user-select:none;} .leaflet-control-layers-toggle {background-image: url("/static/app/img/layers.png"); background-size: 60%;} .leaflet-touch .leaflet-bar {border: 1px solid rgba(0,0,0,0.1);background-color: #000000b8;} .strong {font-weight: 700;line-height: 1.6;font-size: 1.4rem;text-transform: uppercase;}  .leaflet-touch .leaflet-control-layers-toggle {width: 44px;height: 44px;background-color: #000000b8;}  .leaflet-touch .leaflet-bar a {border-bottom-left-radius: 2px;border-bottom-right-radius: 2px;border: 1px solid #000;} .strong{} .leaflet-popup-content-wrapper {width: 180px;text-align: center;height: auto;} .desc{}  .leaflet-popup-content p {margin: 10px 0;} .popupdiv{}
    .js-measuringprompt{color: #000 } .leaflet-touch .leaflet-control-measure .leaflet-control-measure-toggle{width: 30px;height: 30px;border-radius: 1px;border: solid 1px #000;}  </style>'''
    #Adding the elements t
    m.get_root().header.add_child(folium.Element(style_statement))
    m

    m.save('Map/templates/Folium.html')
    context = {'my_map': m}

#=========================================================== Adding Django template tag in the beginning of Webmap template========================================================================
    filename= 'Map/templates/webmap.html'
    line= "{% load staticfiles %} {%load leaflet_tags%} {% leaflet_js%}{% leaflet_css%} <script src='{% static 'leaflet/leaflet/leaflet.js' %}'></script> <link rel='stylesheet' href='{% static 'leaflet/leaflet/leaflet.css' %}'>"
    with open(filename, 'r+') as f:
        content= f.read()
        f.seek(0, 0)
        f.write(line.rstrip('\r\n')+'\n'+ content)

    return render(request, 'Folium.html', context)



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
    contenu= Contact_page.objects.all()
    return render(request,"about.html",{'about':abouts[0],'contact':contacts[0],'tete':tete[0],'list':portfolios[:4],'serv':services, 'part':part,'menu':Menu[0],'contpg':contenu[0]})


def prestations_view(request,prestation_id):
    detailpres= get_object_or_404(Prestations_page, pk=prestation_id)
    services= Prestations_page.objects.all()
    tete=Tete_de_page.objects.all()
    contacts= Pied_de_page.objects.all()
    abouts= About.objects.all()
    Menu=Menu_bar.objects.all()
    services= Prestations_page.objects.all()
    Accueil=Accueil_page.objects.all()
    contenu= Contact_page.objects.all()
    return render(request,"prestations.html",{'presdet':detailpres, 'contact':contacts[0],'tete':tete[0],'about':abouts[0],'menu':Menu[0],'serv':services,'Accueil':Accueil[0],'contpg':contenu[0]})


def introprestation_view(request,*arg,**kwargs):

    services= Prestations_page.objects.all()
    tete=Tete_de_page.objects.all()
    contacts= Pied_de_page.objects.all()
    abouts= About.objects.all()
    Menu=Menu_bar.objects.all()
    services= Prestations_page.objects.all()
    Accueil=Accueil_page.objects.all()
    contenu= Contact_page.objects.all()
    intro= Intro_prestation.objects.all()
    return render(request,"introprestations.html",{'contact':contacts[0],'tete':tete[0],'about':abouts[0],'menu':Menu[0],'serv':services,'Accueil':Accueil[0],'contpg':contenu[0],'intro':intro[0]})
