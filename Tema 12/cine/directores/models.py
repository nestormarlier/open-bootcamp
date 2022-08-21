from django.urls import reverse
from django.db import models
import uuid


class Genre(models.Model):
    nombre = models.CharField(max_length=50, help_text='Ingrese aquí el nombre de género')

    def __str__(self):
        return self.nombre


class Directores(models.Model):
    nombre = models.CharField(max_length=30, help_text='Ingrese nombre del director')
    apellido = models.CharField(max_length=30, help_text='Ingrese apellido del director')
    day_birth = models.DateField(null=True, blank=True)
    nacionalidad = models.CharField(max_length=100)

    def __str__(self):
        return '%s, %s' %(self.apellido, self.nombre)

    def get_absolute_url(self):
        return reverse('director_detail', args=[str(self.id)])

class Peliculas(models.Model):
    titulo = models.CharField(max_length=150, help_text='Ingrese nombre de la película')
    sinopsis = models.TextField(max_length=1000, help_text='Ingrese aquí su sinopsis')
    director = models.ForeignKey('Directores', on_delete=models.SET_NULL, null=True)
    isbn = models.CharField('ISBN', max_length=13,help_text='El ISBN de 13 caracteres')
    genre = models.ManyToManyField(Genre)
    ver = models.CharField(max_length=200, help_text="Dirección web donde se encuentra alojada la película") #se coloco dirección web del Trialer

    def __str__(self):
        return self.titulo

    def get_absolute_url(self):
        return reverse('pelicula_detail', args=[str(self.id)])

class PeliculasInstance(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4(), help_text='Id unico para esta película')
    pelicula = models.ForeignKey('Peliculas', on_delete=models.SET_NULL, null=True)

    TIPO_PELICULA = (
        ('s', 'Serie'),
        ('p', 'Película'),
        ('c', 'Cortometraje'),
        ('d', 'Documental'),
        ('m', 'Miniserie'),
    )

    tipo = models.CharField(max_length=1, choices=TIPO_PELICULA, blank=True, default='p', help_text='Tipo de película')

    class Meta:
        ordering = ['pelicula']

    def __str__(self):
        return'%s %s' %(self.id, self.pelicula.titulo)