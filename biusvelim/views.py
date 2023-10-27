from django.shortcuts import render
from django.views import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
# Create your views here.

class Home(View):
    def get(self, request, *args, **kwargs):
            return render(request, 'index.html')
    

method_decorator(login_required, name='dispatch')
class PerfilList(View):
      def get(self, request, *args, **kwargs):
            perfil = request.user.perfiles.all()

            context = {
                  'perfil': perfil
            }

            return render(request, 'PerfilLista.html', context)