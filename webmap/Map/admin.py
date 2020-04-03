from django.contrib import admin
from .models import Projet, About, Pied_de_page , Message, Services, Contact_page
from leaflet.admin import LeafletGeoAdmin
# Register your models here.

class ProjetAdmin(LeafletGeoAdmin):
    list_display=('Nom','Latitude','Longitude','Département','Services','Adress','Tel','Description_si_disop')
    readonly_fields = ('Latitude','Longitude')
    list_filter= ()

admin.site.register(Projet,ProjetAdmin)
admin.site.register(About)
admin.site.register(Pied_de_page)
admin.site.register(Message)
admin.site.register(Services)
admin.site.register(Contact_page)
