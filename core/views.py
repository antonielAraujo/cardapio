from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

# Create your views here.

## HOME DOS USUÁRIOS
@login_required(login_url='logar/')
def home(request):
    return render(request, 'home.html')

def home_adm(request):
    if request.user.is_staff == 1:
        usuario = request.user.username
        context = {
            'usuario': usuario
        }
        return render(request, 'home_adm.html', context)
    elif request.user.is_staff == 0:
        return redirect(pagina_erro_user)
    
def home_garcon(request):
    usuario = request.user.username
    context = {
        'usuario': usuario
    }  
    return render(request, 'home_garcon.html', context)

### CRIAÇÃO DOS LOGINS

# FUNÇÃO CADASTRO DE USUÁRIO
def cadastrar_usuario(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(logar)
    else:
        form = UserCreationForm()
    context = {
        'form': form
    }
    return render(request, 'cadastrar_usuario.html', context)

# FUNÇÃO LOGAR
def logar(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            usuario = form.get_user()
            login(request, usuario)
            return redirect(home)
    else:
        form = AuthenticationForm()
    context = {
        'form': form
    }
    return render(request, 'logar.html', context)

# FUNÇÃO DESLOGAR
def deslogar(request):
    logout(request)
    return redirect(home)

### FIM DAS FUNÇÕES DE LOGIN

### ÍNICIO DO CRUD DA CATEGORIA

# FUNÇÃO CADASTRAR CATEGORIA
@login_required(login_url='logar/')
def cad_categoria(request):
    categorias = Categoria.objects.all()
    if request.user.is_staff == 1:
        if request.method == 'POST':   
            form = FormCadCategoria(request.POST)
            if form.is_valid():
                form.save()
                return redirect(cad_categoria)
        else:
            form = FormCadCategoria()
        context = {
            'formCadCategoria': form,
            'categorias': categorias
        }
        return render(request, 'cad_categoria.html', context)
    elif request.user.is_staff == 0:
        return redirect(pagina_erro_user)
    

# FUNÇÃO EXIBIR CATEGORIAS
@login_required(login_url='logar/')
def exibir_categorias(request):
    categorias = Categoria.objects.all()
    context = {
        'categorias': categorias
    }
    return render(request, 'exibir_categorias.html', context)

# FUNÇÃO EDITAR CATEGORIA
@login_required(login_url='logar/')
def editar_categoria(request, id_categoria):
    categoria_puxada = Categoria.objects.get(id=id_categoria)
    if request.user.is_staff == 1:
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
    elif request.user.is_staff == 0:
        return redirect(pagina_erro_user)


# FUNÇÃO EXCLUIR CATEGORIA
@login_required(login_url='logar/')
def excluir_categoria(request, id_categoria):
    if request.user.is_staff == 1:
        categoria_puxada = Categoria.objects.get(id=id_categoria)
        categoria_puxada.delete()
        return redirect(exibir_categorias)
    elif request.user.is_staff == 0:
        return redirect(pagina_erro_user)
    
### FIM DO CRUD DE CATEGORIA


### INÍCIO DO CRUD DE COMIDAS

# FUNÇÃO CADASTRO DE COMIDAS
@login_required(login_url='logar/')
def cad_comida(request):
    comidas = Comida.objects.all()
    if request.user.is_staff == 1:
        if request.method == 'POST':
            form = FormCadComida(request.POST, request.FILES)
            if form.is_valid():            
                form.save()
                return redirect(cad_comida)
        else:
            form = FormCadComida()
        return render(request, 'cad_comida.html', {'formCadComida': form, 'comidas': comidas})
    elif request.user.is_staff == 0:
        return redirect(pagina_erro_user)

# FUNÇÃO EXIBIR COMIDAS
@login_required(login_url='logar/')
def exibir_comidas(request):
    comidas = Comida.objects.all()
    context = {
        'comidas': comidas
    }
    return render(request, 'exibir_comidas.html', context)

# FUNÇÃO EDITAR COMIDA
@login_required(login_url='logar/')
def editar_comida(request, id_comida):
    comida_puxada = Comida.objects.get(id=id_comida)
    if request.user.is_staff == 1:
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
    elif request.user.is_staff == 0:
        return redirect(pagina_erro_user)
    
# FUNÇÃO EXCLUIR COMIDA
@login_required(login_url='logar/')
def excluir_comida(request, id_comida):
    if request.user.is_staff == 1:
        comida = Comida.objects.get(id=id_comida)
        comida.delete()
    return redirect(exibir_comidas)


### FIM DO CRUD CADASTRO DE COMIDAS

### INÍCIO DO CRUD DE PEDIDOS

# FUNÇÃO INICIAR PEDIDO
@login_required(login_url='logar/')
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
@login_required(login_url='logar/')
def exibir_pedidos(request):
    context = {
        'pedidos': Pedido.objects.all()
    }
    return render(request, 'exibir_pedidos.html', context)

# FUNÇÃO ADICIONAR COMIDA EM PEDIDOS
@login_required(login_url='logar/')
def adicionar_comida(request, id_pedido):
    pedido = Pedido.objects.get(id=id_pedido)
    comidas = Comida.objects.all()
    if pedido.pagamento == True:
        return redirect(pagina_erro)
    elif request.method == 'POST':
        form = FormComidasPedidos(request.POST)
        if form.is_valid():
            lancamento = form.save(commit=False)
            lancamento.pedido = pedido
            lancamento.save()
            return redirect(exibir_pedidos)
    else:
        form = FormComidasPedidos()
    context = {
        'form': form,
        'pedido': pedido,
        'comidas': comidas
    }
    return render(request, 'adicionar_comida.html', context)

# FUNÇÃO RESUMO PEDIDO
@login_required(login_url='logar/')
def resumo_pedido(request, id_pedido):
    resumo = ComidasPedidos.objects.filter(pedido=id_pedido)
    context = {
        'resumo': resumo
    }
    return render(request, 'resumo_pedido.html', context)

# FUNÇÃO EDITAR RESUMO DO PEDIDO
@login_required(login_url='logar/')
def editar_resumo_pedido(request, id_comidas_pedidos):
    comida_pedido = ComidasPedidos.objects.get(id=id_comidas_pedidos)
    if comida_pedido.pedido.pagamento == True:
         return redirect(pagina_erro)
    elif request.method == 'POST':
        form = FormComidasPedidos(request.POST, instance=comida_pedido)
        if form.is_valid():
            form.save()
            return redirect(exibir_pedidos)
    else:
        form = FormComidasPedidos(instance=comida_pedido)
    context = {
        'form': form,
        'comida_pedido': comida_pedido
    }
    return render(request, 'editar_resumo_pedido.html', context)

# FUNÇÃO EXCLUIR ITEM DE UM PEDIDO
@login_required(login_url='logar/')
def excluir_item_pedido(request, id_comidas_pedidos):
    comida_pedido = ComidasPedidos.objects.get(id=id_comidas_pedidos)
    if comida_pedido.pedido.pagamento == True:
         return redirect(pagina_erro)
    else:
        comida_pedido.delete()
        return redirect(exibir_pedidos)
    
# FUNÇÃO EXCLUIR PEDIDO
@login_required(login_url='logar/')
def excluir_pedido(request, id_pedido):
    pedido = Pedido.objects.get(id=id_pedido)
    if pedido.pagamento == True:
        return redirect(pagina_erro)
    pedido.delete()
    return redirect(exibir_pedidos)

# FUNÇÃO FECHAR PEDIDO
@login_required(login_url='logar/')
def fechar_pedido(request, id_pedido):
    pedido = Pedido.objects.get(id=id_pedido)
    if pedido.pagamento == True:
        return redirect(pagina_erro)
    elif pedido.pagamento == False:
        pedido.pagamento = True
        pedido.save()
        return redirect(exibir_pedidos)

# FUNÇÃO PÁGINA DE ERRO
def pagina_erro(request):
    return render(request, 'pagina_erro.html')

# FUNÇÃO PÁGINA ERRO PARA USUÁRIO
def pagina_erro_user(request):
    usuario = request.user.username
    context = {
        'usuario': usuario
    }
    return render(request, 'pagina_erro_user.html', context)
