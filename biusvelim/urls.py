from django.urls import path 
from .views import Home, PerfilList
app_name = 'biusvelim'

urlpatterns = [
    path('', Home.as_view(), name='Home'),
    path('profiles', PerfilList.as_view(), name='perfil_list')
]