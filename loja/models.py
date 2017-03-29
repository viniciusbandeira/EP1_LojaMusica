from django.db import models


class Genero(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)

class Artista(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    biografia = models.CharField(max_length=400)
    generos = models.ManyToManyField(Genero)



class Album(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    ano = models.IntegerField()
    astistas = models.ManyToManyField(Artista)

