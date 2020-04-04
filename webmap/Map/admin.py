from django.contrib import admin
from .models import Webmap, About, Pied_de_page , Message, Prestations_page, Contact_page, Tete_de_page, Accueil_page
from leaflet.admin import LeafletGeoAdmin
# Register your models here.

class WebmapAdmin(LeafletGeoAdmin):
    list_display=('Nom','Latitude','Longitude','Département','Services','Adress','Tel','Description_si_disop')
    readonly_fields = ('Latitude','Longitude')
    list_filter= ()

admin.site.register(Webmap,WebmapAdmin)
admin.site.register(About)
admin.site.register(Pied_de_page)
admin.site.register(Message)
admin.site.register(Prestations_page)
admin.site.register(Contact_page)
admin.site.register(Tete_de_page)
admin.site.register(Accueil_page)
