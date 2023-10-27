from django.contrib import admin
from biusvelim.models import Pelicula, Video, Perfil, CustomUser
# Register your models here.
admin.site.register(Pelicula)
admin.site.register(Video)
admin.site.register(Perfil)
admin.site.register(CustomUser)