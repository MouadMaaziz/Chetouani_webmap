from django.contrib import admin
from .models import Projet, About, Contact , Message
from leaflet.admin import LeafletGeoAdmin
# Register your models here.

class ProjetAdmin(LeafletGeoAdmin):
    list_display=('Nom','Latitude','Longitude','Description','Type')
    readonly_fields = ('Latitude','Longitude')
    list_filter= ()

admin.site.register(Projet,ProjetAdmin)
admin.site.register(About)
admin.site.register(Contact)
admin.site.register(Message)
