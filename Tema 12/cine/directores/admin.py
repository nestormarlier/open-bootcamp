from django.contrib import admin

from .models import Peliculas, PeliculasInstance,Genre, Directores

admin.site.register(Peliculas)
admin.site.register(PeliculasInstance)
admin.site.register(Genre)
admin.site.register(Directores)
