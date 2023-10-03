from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

# Create your views here.

def home(request):
    return render(request, 'home.html')

def home_adm(request):
    return render(request, 'home_adm.html')

def home_garcon(request):
    return render(request, 'home_garcon.html')

def cad_categoria(request):
    categorias = Categoria.objects.all()
    if request.method == 'POST':
        form = FormCadCategoria(request.POST)
        if form.is_valid():
            form.save()
            return redirect(cad_categoria)
    else:
        form = FormCadCategoria()
    return render(request, 'cad_categoria.html', {'formCadCategoria': form, 'categorias': categorias})

def cad_comida(request):
    comidas = Comida.objects.all()
    if request.method == 'POST':
        form = FormCadComida(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(cad_comida)
    else:
        form = FormCadComida()
    return render(request, 'cad_comida.html', {'formCadComida': form, 'comidas': comidas})

def pedido(request):
    if request.method == 'POST':
        form = FormPedido(request.POST)
        if form.is_valid():
            form.save()
            return redirect(comidas_pedidos)
    else:
        form = FormPedido()
    return render(request, 'pedido.html', {'formPedido': form})

def comidas_pedidos(request):
    comidas = Comida.objects.all()
    pedido = Pedido.objects.all()
    
    if request.method == 'POST':
        form = FormComidasPedidos(request.POST)
        if form.is_valid():
            form.save()
            return redirect(pedido_fechado)
    else:
        form = FormComidasPedidos()
    return render(request, 'comidas_pedidos.html', {'formComidasPedidos': form, 'comidas': comidas, 'pedido': pedido})

def pedido_fechado(request, id_pedido):
    pedidos = Pedido.objects.get(id=id_pedido)  
    return render(request, 'pedido_fechado.html', {'pedidos': pedidos})