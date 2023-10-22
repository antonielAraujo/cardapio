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
    path('novo_pedido/', novo_pedido, name='novo_pedido'),
    path('exibir_pedidos/', exibir_pedidos, name='exibir_pedidos'),
    path('editar_pedido/<int:id_pedido>', editar_pedido, name='editar_pedido'),
    path('adicionar_comida/<int:id_pedido>', adicionar_comida, name='adicionar_comida'),
    path('resumo_pedido/<int:id_pedido>', resumo_pedido, name='resumo_pedido'),
    path('excluir_pedido/<int:id_pedido>', excluir_pedido, name='excluir_pedido'),
    path('fechar_pedido/<int:id_pedido>', fechar_pedido, name='fechar_pedido'),
    path('pagina_erro/', pagina_erro, name='pagina_erro')
    # path('exibir_pedidos_fechados/', exibir_pedidos_fechados, name='exibir_pedidos_fechados')



] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)