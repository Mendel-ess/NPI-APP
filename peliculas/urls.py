from django.urls import path
from .views import PeliculaList, PeliculaDetail

urlpatterns = [
        path('', PeliculaList.as_view(), name='pelicula_list'),
        path('<int:pk>', PeliculaDetail.as_view(), name='pelicula_detail')
    ]
