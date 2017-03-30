from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Artista, Album, Genero, Musica, Genero


def index(request):
    artistas = Artista.objects.all()
    context = {'artistas': artistas}
    return render(request, 'loja/index.html', context)

def artista(request,id):
    artista = Artista.objects.get(id=id)
    context = {'artista': artista}

    return render(request, 'loja/artista.html', context)

def artista_like(request,id):
    artista = Artista.objects.get(id=id)
    artista.numero_gostei+=1
    artista.save()

    return redirect('artista', id=artista.id)