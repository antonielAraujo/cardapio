from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # ÍNICIO DO SITE
    path('', home, name='home'),
    path('home_adm/', home_adm, name='home_adm'),
    path('home_garcom/', home_garcon, name='home_garcon'),
    
    # CRUD DA CATEGORIA
    path('cad_categoria/', cad_categoria, name='cad_categoria'),
    path('exibir_categorias/', exibir_categorias, name='exibir_categorias'),
    path('editar_categoria/<int:id_categoria>', editar_categoria, name='editar_categoria'),
    path('excluir_categoria/<int:id_categoria>', excluir_categoria, name='excluir_categoria'),
    
    # CRUD DA COMIDA
    path('cad_comida/', cad_comida, name='cad_comida'),
    path('exibir_comidas/', exibir_comidas, name='exibir_comidas'),
    path('editar_comida/<int:id_comida>', editar_comida, name='editar_comida'),
    path('excluir_comida/<int:id_comida>', excluir_comida, name='excluir_comida'),
    
    # CRUD DOS PEDIDOS
    

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)