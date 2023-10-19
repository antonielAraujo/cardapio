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

### ÍNICIO DO CRUD DA CATEGORIA

# FUNÇÃO CADASTRAR CATEGORIA
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

# FUNÇÃO EXIBIR CATEGORIAS
def exibir_categorias(request):
    categorias = Categoria.objects.all()
    context = {
        'categorias': categorias
    }
    return render(request, 'exibir_categorias.html', context)

# FUNÇÃO EDITAR CATEGORIA
def editar_categoria(request, id_categoria):
    categoria_puxada = Categoria.objects.get(id=id_categoria)
    if request.method == 'POST':
        form = FormCadCategoria(request.POST, instance=categoria_puxada)
        if form.is_valid():
            form.save()
            return redirect(exibir_categorias)
    else:
        form = FormCadCategoria(instance=categoria_puxada)
    context = {
        'form' : form,
        'categoria': categoria_puxada
    }
    return render(request, 'editar_categoria.html', context)

# FUNÇÃO EXCLUIR CATEGORIA
def excluir_categoria(request, id_categoria):
    categoria_puxada = Categoria.objects.get(id=id_categoria)
    categoria_puxada.delete()
    return redirect(exibir_categorias)
### FIM DO CRUD DE CATEGORIA


### INÍCIO DO CRUD DE COMIDAS

# FUNÇÃO CADASTRO DE COMIDAS
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

# FUNÇÃO EXIBIR COMIDAS
def exibir_comidas(request):
    comidas = Comida.objects.all()
    context = {
        'comidas': comidas
    }
    return render(request, 'exibir_comidas.html', context)

# FUNÇÃO EDITAR COMIDA
def editar_comida(request, id_comida):
    comida_puxada = Comida.objects.get(id=id_comida)
    if request.method == 'POST':
        form = FormCadComida(request.POST, request.FILE, instance=comida_puxada)
        if form.is_valid():
            form.save()
            return redirect(exibir_comidas)
    else:
        form = FormCadComida(request.FILE, instance=comida_puxada)
    context = {
        'form': form,
        'comida': comida_puxada
    }
    return render(request, 'editar_comida.html', context)


### FIM DO CRUD CADASTRO DE COMIDAS

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