import imp
from django.shortcuts import redirect, render
from django.views import View
from django.conf import settings
from django.http import FileResponse, HttpResponse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .forms import ProfileForm
from .models import Perfil, Pelicula
import os

class Home(View):
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('biusvelim:perfil_list')
        return render(request, 'index.html')

method_decorator(login_required, name='dispatch')
class PerfilList(View):
    def get(self, request, *args, **kwargs):
        
        perfiles = request.user.perfiles.all()

        context = {
            'perfiles': perfiles
        }
        return render(request, 'PerfilLista.html', context)

method_decorator(login_required, name='dispatch')
class CrearPerfil(View):
    def get(self, request, *args, **kwargs):
        form = ProfileForm()
        context = {
            'form':form
        }
        return render(request, 'crearperfil.html', context)

    def post(self, request, *args, **kwargs):
        form = ProfileForm(request.POST or None)
        if form.is_valid():
            perfil = Perfil.objects.create(**form.cleaned_data)
            if perfil:
                request.user.profiles.add(perfil)
                return redirect('biusvelim:perfil_list')
        context = {
            'form':form
        }
        return render(request, 'crearperfil.html', context)

method_decorator(login_required, name='dispatch')
class PeliculaList(View):
    def get(self, request, perfil_id, *args, **kwargs):
        try:
            perfil = Perfil.objects.get(uuid=perfil_id)
            peliculas = Pelicula.objects.filter(edad_limite=perfil.edad_limite)
            if perfil not in request.user.perfiles.all():
                return redirect('biusvelim:perfil_list')

            context = {
            'peliculas':peliculas
            }

            return render(request, 'peliculalista.html', context)
        except Perfil.DoesNotExist:
            return redirect('biusvelim:perfil_list')

method_decorator(login_required, name='dispatch')
class DetallePelicula(View):
    def get(self, request, pelicula_id, *args, **kwargs):
        try:
            pelicula = Pelicula.objects.get(uuid=pelicula_id)
            
            context = {
                'pelicula': pelicula
            }

            return render(request, 'detallepelicula.html', context)
        except Pelicula.DoesNotExist:
            return redirect('biusvelim:perfil_list')

method_decorator(login_required, name='dispatch')
class RepoPeli(View):
    def get(self, request, movie_id, *args, **kwargs):
        try:
            pelicula = Pelicula.objects.get(uuid=movie_id)
            pelicula = pelicula.video.values()
            
            context = {
                'pelicula':list(pelicula)
            }

            return render(request, 'repeli.html', context)
        except Pelicula.DoesNotExist:
            return redirect('biusvelim:perfil_list')
        
class DescargarDocumentacion(View):
    def get(self, request, file_name):
        file_path = os.path.join(settings.MEDIA_ROOT, file_name)
        if os.path.exists(file_path):
            with open(file_path, 'rb') as file:
                response = FileResponse(file)
                response['Content-Disposition'] = f'attachment; filename="{file_name}"'
                return response
        else:
            return HttpResponse('El archivo no existe.', status=404)