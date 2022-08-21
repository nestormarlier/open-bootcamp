from django.urls import re_path as url
from . import  views

urlpatterns=[
    url(r'^$', views.index, name='index'),
    url('peliculas/', views.peliculas, name='pelis'),
    url('generos/', views.generos, name='genre')
]