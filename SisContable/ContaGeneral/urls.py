from django.conf.urls import url
from .views import *
from django.contrib.auth import authenticate, login
from django.conf.urls import url 
from ContaGeneral import views

urlpatterns= [
    url(r'^$', principal, name='main'),
    url(r'^catalogo/$',views.catalogo),
    url(r'^diario/$',views.diario),
    url(r'^empresa/$',views.empresa),
]