from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

# Create your views here.

def home(request):
    return render(request, 'home.html')

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
