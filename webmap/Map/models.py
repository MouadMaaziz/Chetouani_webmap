from django.db import models
from django.contrib.gis.db import models
from django.db.models import Manager as GeoManager

# Create your models here.
class Projet(models.Model):


    Nom= models.CharField(max_length=50)
    geom= models.PointField(srid=4326, blank= True,default=None)
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
         super(Projet, self).save(*args, **kwargs)

    def save(self, *args, **kwargs):
         self.link  =self.img.url   #make a way to the media folder where images are being saved
         super(Projet, self).save(*args, **kwargs)



class About(models.Model):
    Photo_Personel= models.ImageField(null=True)
    Photos_ArrierePlan= models.ImageField(null=True)
    Photos_dentreprise= models.ImageField(null=True)
    Introduction = models.TextField(max_length=300)
    notre_Histoire = models.TextField(max_length=800)
    qui_Somme_Nous = models.TextField(max_length=300)
    nos_Valeurs = models.TextField(max_length=300)
    nos_Missions = models.TextField(max_length=300)
    notre_Vision = models.TextField(max_length=300)
    def __str__(self):
        return self.Introduction

class Contact(models.Model):
    Adress= models.TextField(null=True, blank= True)
    Phone = models.TextField(max_length=25, blank= True)
    Email = models.TextField(max_length=30, blank= True)
    facebookPage= models.TextField(max_length=80, null=True, blank= True)
    instaProfile= models.TextField(max_length=80, null=True , blank= True)
    linkedIn= models.TextField(max_length=80, null=True , blank= True)
    youtubeChannel= models.TextField(max_length=80, null=True, blank= True)


    def __str__(self):
        return self.Adress


class Message(models.Model):
    Email= models.EmailField()
    Name= models.CharField(max_length= 120)
    message= models.CharField(max_length= 700 )

    def __str__(self):
        return self.Name

class Services(models.Model):
        Nom= models.CharField(max_length= 120)
        Description= models.CharField(max_length= 520)
        Icon= models.CharField(max_length= 50,default='fas fa-' )

        def __str__(self):
            return self.Nom
