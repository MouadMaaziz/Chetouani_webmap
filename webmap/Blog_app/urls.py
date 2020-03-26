from django.urls import path, include
from . import views



urlpatterns = [

    path('', views.portfolio_view,name='portfolio'),
    path('<int:blog_id>/',views.detail_view,name='detail'),
    



]
