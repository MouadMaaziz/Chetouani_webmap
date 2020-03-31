
from django.db import models
from  ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.


class Portfolio(models.Model):
    Titre = models.CharField(max_length=80)
    pub = models.CharField(max_length=40, null=True, blank=True,default='M.Y.CHETOUANI')
    Contenu = RichTextUploadingField()
    link = models.URLField(null=True, blank=True)
    Photo = models.ImageField(upload_to='')
    Date_de_pub = models.DateTimeField(auto_now=False,null=True)
    draft = models.BooleanField(default=False)
    Mot_Cle= models.CharField(max_length=30,null=True)



    def __str__(self):
        return self.Titre

    def summary(self):
        return self.Contenu[:200]

    def Date_cus(self):
        return self.Date_de_pub.strftime('%A %d %b')
