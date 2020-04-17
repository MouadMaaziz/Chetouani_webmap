from django.contrib import admin
from django.urls import path, include
from Map.views import *
from djgeojson.views import GeoJSONLayerView
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [

    path('admin/', admin.site.urls),
    path('', home_view,name='home'),
    path('home/', home_view,name='home'),
    path('webmap/', webmap_view,name='webmap'),
    path('data/', GeoJSONLayerView.as_view(model= Webmap, properties=('Nom','Département','Services','link','Adress','Tel','Description_si_disop')),name='data'),
    path('portfolio/', include('Blog_app.urls'),name='portfolio'),
    path('contact/', contact_view,name='contact'),
    path('about/', about_view,name='about'),
    #path('prestations/', prestations_view,name='prestations'),
    path('<int:prestation_id>/', prestations_view,name='presdetails'),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('introprestation/', introprestation_view,name='introprestation'),

] + static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)


urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
