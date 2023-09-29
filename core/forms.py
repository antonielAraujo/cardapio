from django.forms import ModelForm
from .models import *
from django import forms

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

class FormComidasPedidos(ModelForm):
    class Meta:
        model = ComidasPedidos
        fields = ['comida', 'pedido', 'quantidade']