from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    # ex: /artista/5/
    url(r'^artista/(?P<id>[0-9]+)/$', views.artista, name='artista'),
    url(r'^artista/(?P<id>[0-9]+)/like/$', views.artista_like, name='artista_like'),
]