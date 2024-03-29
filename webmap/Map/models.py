from django.db import models
from django.contrib.gis.db import models
from django.db.models import Manager as GeoManager
from  ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.
class Webmap(models.Model):

    geom= models.PointField(srid=4326, blank= True,default=None)
    Nom= models.CharField(max_length=50)
    Département= models.CharField(max_length=300,null=False,default="",blank= True)
    Services= models.CharField(max_length=200, null=False,default="",blank= True)
    Description_si_disop= models.CharField(max_length=200, null=False,default="",blank= True)
    Adress= models.CharField(max_length=200,default="",blank= True)
    Tel= models.CharField(max_length=200,default="",blank= True)
    Latitude = models.FloatField(max_length=8,default=30)
    Longitude = models.FloatField(max_length=8,default=-8)
    img = models.ImageField(null=True)
    link = models.URLField(null=True, blank=True)
    object= GeoManager()

    def save(self, *args, **kwargs):
         self.Latitude  = self.geom.y
         self.Longitude = self.geom.x
         super(Webmap, self).save(*args, **kwargs)

    def save(self, *args, **kwargs):
         self.link  =self.img.url   #make a way to the media folder where images are being saved
         super(Webmap, self).save(*args, **kwargs)

class Contact_page(models.Model):

    Whatsp = models.CharField(max_length=200)
    Phrase_formulaire= models.CharField(max_length=200,default='Enovoyz-nous un message')
    demande_nom = models.CharField(max_length=200,default='dites nous votre nom')
    demande_email = models.CharField(max_length=200,default='votre email')
    demande_message = models.CharField(max_length=200,default='tapez nous un message')
    section_adress= models.CharField(null=True, blank= True,max_length=800,default='Adress')
    contenu_adress= models.TextField(null=True, blank= True,max_length=800)
    section_phone= models.CharField(null=True, blank= True,max_length=800,default='Telephone')
    contenu_phone= models.TextField(null=True, blank= True)
    section_email= models.CharField(null=True, blank= True,max_length=800,default='Nous contacter')
    contenu_email= models.TextField(null=True, blank= True)

    def __str__(self):
        return self.demande_nom

class Accueil_page(models.Model):

    video_phrase1 = models.CharField(max_length=200,default='WE ARE HERE TO CREATE A LASTING RELATIONSHIP WITH YOU')
    video_titre = models.CharField(max_length=200,default='STE CHETOUANI TOPOGRAPHIE & GEOMATIQUE')
    video_phrase2 = models.CharField(max_length=200,default='GEOMATIQUE- AMENAGEMENT- EXPERTISE FINANCIER')
    Intro = RichTextUploadingField(max_length=100000)
    prestations_section= models.CharField(max_length=200,default='Nos prestations du service')
    actualite_section= models.CharField(max_length=200,default='Nos actualites')
    def __str__(self):
        return self.video_titre



class About(models.Model):
    mini_phrase= models.CharField(max_length=300,default='~Nos simples interets ~')
    Phrase_principale= models.CharField(max_length=300,default='Nous sommes des')
    mot_defilant_1= models.CharField(max_length=300,default='Topographes')
    mot_defilant_2= models.CharField(max_length=300,default='Géomaticiens')
    mot_defilant_3= models.CharField(max_length=300,default='Développeurs')
    Photo_Personel= models.ImageField(null=True)
    Photos_ArrierePlan= models.ImageField(null=True)
    Info_titre= models.CharField(max_length=1000,default='A propos de Ste.Chetouani.')
    Introduction = RichTextUploadingField(max_length=100000)
    Titre_carte= models.CharField(max_length=300,default='ou sommes nou aujourdhui')
    de_nous= models.CharField(max_length=300,default='qui somme nous ?')
    qui_Somme_Nous = RichTextUploadingField(max_length=100000)
    valeurs= models.CharField(max_length=300,default='nos valeurs')
    nos_Valeurs = RichTextUploadingField(max_length=100000)
    missions= models.CharField(max_length=300,default='nos missions')
    nos_Missions = RichTextUploadingField(max_length=100000)
    vision= models.CharField(max_length=300,default='notre vision')
    notre_Vision = RichTextUploadingField(max_length=100000)
    nos_partenaire= models.CharField(max_length=300,default='Nos clients et partenaires')
    def __str__(self):
        return self.Introduction

class Tete_de_page(models.Model):
    Accueil= models.CharField(null=True, blank= True,max_length= 80)
    Contact= models.CharField(null=True, blank= True,max_length= 80)
    A_propos= models.CharField(null=True, blank= True,max_length= 80)
    Prestations= models.CharField(null=True, blank= True,max_length= 80)
    Actualite= models.CharField(null=True, blank= True,max_length= 80)


    def __str__(self):
        return self.Accueil


class Menu_bar(models.Model):
    Accueil= models.CharField(null=True, blank= True,max_length= 80, default= 'Accueil')
    Contact= models.CharField(null=True, blank= True,max_length= 80, default= 'Contact')
    A_propos= models.CharField(null=True, blank= True,max_length= 80, default= 'A_propos')
    Prestations= models.CharField(null=True, blank= True,max_length= 80, default= 'prestations')
    Actualite= models.CharField(null=True, blank= True,max_length= 80, default= 'Actualite')


    def __str__(self):
        return self.Accueil

class Pied_de_page(models.Model):
    section_1= models.TextField(null=True, blank= True,default='Qui somme nous?')
    contenu_1= models.TextField(null=True, blank= True)
    section_2= models.TextField(null=True, blank= True,default='Ou nous trouver ?')
    contenu_2= models.TextField(null=True, blank= True)
    section_3= models.TextField(null=True, blank= True,default='Nous contacter')
    contenu_3= models.TextField(null=True, blank= True)
    contenu_3_ligne2= models.TextField(null=True, blank= True)
    facebookPage= models.CharField(max_length=80, null=True, blank= True,default='https://www.facebook.com/chetopgeo/')
    instaProfile= models.CharField(max_length=80, null=True , blank= True)
    linkedIn= models.CharField(max_length=80, null=True , blank= True)
    youtubeChannel= models.CharField(max_length=80, null=True, blank= True)


    def __str__(self):
        return self.section_1


class Message(models.Model):
    Email= models.EmailField()
    Name= models.CharField(max_length= 120)
    message= models.CharField(max_length= 700 )

    def __str__(self):
        return self.Name

class Partenairs(models.Model):
    Nom= models.CharField(max_length= 120)
    Image= models.ImageField(null=True)
    Lien= models.CharField(max_length= 520)

    def __str__(self):
        return self.Nom

class Prestations_page(models.Model):
        Titre = models.CharField(max_length=80)
        Description= models.TextField(max_length= 1020)
        Icon= models.CharField(max_length= 50,default='fas fa-' )
        Introduction= RichTextUploadingField()
        sous_titre1= models.CharField(max_length=1000, default="", blank= True)
        par1= RichTextUploadingField( null=True, blank= True)
        sous_titre2= models.CharField(max_length=1000, default="", blank= True )
        par2= RichTextUploadingField( null=True, blank= True)
        sous_titre3= models.CharField(max_length=1000, default="", blank= True)
        par3= RichTextUploadingField( null=True, blank= True)
        sous_titre4= models.CharField(max_length=1000, default="", blank= True)
        par4= RichTextUploadingField( null=True, blank= True)
        sous_titre5= models.CharField(max_length=1000, default="", blank= True)
        par5= RichTextUploadingField( null=True, blank= True)
        sous_titre6= models.CharField(max_length=1000, default="", blank= True)
        par6= RichTextUploadingField( null=True, blank= True)
        link = models.URLField(null=True, blank=True)
        Photo = models.ImageField(upload_to='')

        def __str__(self):
            return self.Titre

class Intro_prestation(models.Model):
    Introduction= RichTextUploadingField( null=True, blank= True)
    Image= models.ImageField(upload_to='')
    def __str__(self):
        return self.Introduction
