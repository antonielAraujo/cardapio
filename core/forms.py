from django.forms import ModelForm
from .models import *
from django import forms
from django.forms import DateInput

class FormCadCategoria(ModelForm):
    class Meta:
        model = Categoria
        fields = ['nome']
        labels = {
            'nome': 'Categoria'
        }

class FormCadComida(ModelForm):
    class Meta:
        model = Comida
        fields = ['nome', 'descricao', 'preco', 'estoque', 'imagem', 'categoria']

class FormPedido(ModelForm):
    class Meta:
        model = Pedido
        fields = ['data', 'pagamento']
        widgets = {
            'data': DateInput(attrs={'type':'date'})
        }

class FormComidasPedidos(ModelForm):
    class Meta:
        model = ComidasPedidos
        fields = ['pedido','comida', 'quantidade']