from django.urls import path 
from .views import Home, PerfilList, CrearPerfil, PeliculaList, DetallePelicula, RepoPeli
app_name = 'biusvelim'

urlpatterns = [
    path('', Home.as_view(), name="Home"),
    path('profiles/', PerfilList.as_view(), name="perfil_list"),
    path('profiles/crear/', CrearPerfil.as_view(), name="crear_perfil"),
    path('ver/<str:perfil_id>/', PeliculaList.as_view(), name="pelicula_list"),
    path('ver/detalle/<str:pelicula_id>/', DetallePelicula.as_view(), name="detalle_pelicula"),
    path('ver/play/<str:pelicula_id>/', RepoPeli.as_view(), name="rep_pelicula"),
]