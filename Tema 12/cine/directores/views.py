from django.shortcuts import render

from .models import Peliculas, PeliculasInstance, Genre, Directores
def index(request):
    return render(request,'directores.html',
                  context={
                      'cant_directores': Directores.objects.all().count(),
                      'cant_peliculas': Peliculas.objects.all().count(),
                      'directores': Directores.objects.all().order_by('apellido'),
                      'peliculas': Peliculas.objects.all().order_by('titulo')
                  })

def peliculas(request):
    return render(request, 'peliculas.html',
                  context={
                      'movies': Peliculas.objects.all().order_by('titulo'),
                      'cant_peliculas': Peliculas.objects.all().count(),
                  })

def generos(request):
    return render(request, 'generos.html',
                  context={
                      'generos': Genre.objects.all().order_by('nombre'),
                      'cant_generos': Genre.objects.all().count(),
                  })
