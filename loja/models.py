from django.db import models


class Genero(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)

class Artista(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    biografia = models.CharField(max_length=400)
    generos = models.ManyToManyField(Genero)
    numero_gostei = models.IntegerField(default=0)

class Album(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    ano = models.IntegerField()
    astistas = models.ManyToManyField(Artista)

class Musica(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    album = models.ForeignKey(Album,on_delete=models.CASCADE)