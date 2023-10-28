from django.forms import ModelForm
from biusvelim.models import Perfil

class ProfileForm(ModelForm):
    class Meta:
        model = Perfil
        exclude = ['uuid']