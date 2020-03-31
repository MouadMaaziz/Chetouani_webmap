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
    path('data/', GeoJSONLayerView.as_view(model= Projet, properties=('Nom','Département','Services','link','Adress','Tel','Description_si_disop')),name='data'),
    path('portfolio/', include('Blog_app.urls'),name='portfolio'),
    path('contact/', contact_view,name='contact'),
    path('about/', about_view,name='about'),
    path('assistance/', assistance_view,name='assistance'),
    path('topographie/', assistance_view,name='topographie'),
    path('geomatique/', assistance_view,name='geomatique'),
    path('formations/', assistance_view,name='formations'),
    path('ckeditor/', include('ckeditor_uploader.urls')),

] + static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)


urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
