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
    Intro = models.TextField(max_length=800)
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
    Photos_dentreprise= models.ImageField(null=True)
    Info_titre= models.CharField(max_length=300,default='A propos de Ste.Chetouani.')
    Introduction = models.TextField(max_length=300)
    notre_Histoire = models.TextField(max_length=800)
    qui_Somme_Nous = models.TextField(max_length=300)
    nos_Valeurs = models.TextField(max_length=300)
    nos_Missions = models.TextField(max_length=300)
    notre_Vision = models.TextField(max_length=300)
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

class Prestations_page(models.Model):
        Titre = models.CharField(max_length=80)
        Description= models.TextField(max_length= 520)
        Icon= models.CharField(max_length= 50,default='fas fa-' )
        Contenu = RichTextUploadingField()
        link = models.URLField(null=True, blank=True)
        Photo = models.ImageField(upload_to='')

        def __str__(self):
            return self.Titre
