from django.shortcuts import render

# Create your views here.

from django.views.generic import ListView, DetailView
from .models import Pelicula

class PeliculaList(ListView):
    model = Pelicula
    


class PeliculaDetail(DetailView):
    model = Pelicula
