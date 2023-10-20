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
        form = FormCadComida(request.POST, request.FILES, instance=comida_puxada)
        if form.is_valid():
            form.save()
            return redirect(exibir_comidas)
    else:
        form = FormCadComida(instance=comida_puxada)
    context = {
        'form': form,
        'comida': comida_puxada
    }
    return render(request, 'editar_comida.html', context)

# FUNÇÃO EXCLUIR COMIDA
def excluir_comida(request, id_comida):
    comida = Comida.objects.get(id=id_comida)
    comida.delete()
    return redirect(exibir_comidas)


### FIM DO CRUD CADASTRO DE COMIDAS

### INÍCIO DO CRUD DE PEDIDOS

# FUNÇÃO INICIAR PEDIDO
def novo_pedido(request):
    if request.method == 'POST':
        form = FormPedido(request.POST)
        if form.is_valid():
            form.save()
            return redirect(exibir_pedidos)
    else:
        form = FormPedido()
    context = {
        'form': form
    }
    return render(request, 'novo_pedido.html', context)

# FUNÇÃO EXIBIR TODOS OS PEDIDOS
def exibir_pedidos(request):
    context = {
        'pedidos': Pedido.objects.all()
    }
    return render(request, 'exibir_pedidos.html', context)

# FUNÇÃO EDITAR PEDIDO
def editar_pedido(request, id_pedido):
    pedido = Pedido.objects.get(id=id_pedido)
    if request.method == 'POST':
        form = FormPedido(request.POST, instance=pedido)
        if form.is_valid():
            form.save()
            return redirect(exibir_pedidos)
    else:
        form = FormPedido(instance=pedido)
    context = {
        'form': form,
        'pedido': pedido
    }
    return render(request, 'editar_pedido.html', context)

# FUNÇÃO ADICIONAR COMIDA EM PEDIDOS
def adicionar_comida(request, id_pedido):
    pedido = Pedido.objects.get(id=id_pedido)
    comidas = Comida.objects.all()
    if request.method == 'POST':
        form = FormComidasPedidos(request.POST, instance=pedido)
        if form.is_valid():
            form.save()
            return redirect(exibir_pedidos)
    else:
        form = FormComidasPedidos(instance=pedido)
    context = {
        'form': form,
        'pedido': pedido,
        'comdidas': comidas
    }
    return render(request, 'adicionar_comida.html', context)