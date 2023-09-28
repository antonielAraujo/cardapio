from django.forms import ModelForm
from .models import *

class FormCadCategoria(ModelForm):
    class Meta:
        model = Categoria
        fields = ['nome']