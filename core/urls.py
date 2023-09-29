from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('', home, name='home'),
    path('home_adm/', home_adm, name='home_adm'),
    path('home_garcom/', home_garcon, name='home_garcon'),
    path('cad_categoria/', cad_categoria, name='cad_categoria'),
    path('cad_comida/', cad_comida, name='cad_comida'),
    path('pedido/', pedido, name='pedido'),
    path('comidas_pedidos', comidas_pedidos, name='comidas_pedidos'),
    path('pedido_fechado/<int:id_pedido>', pedido_fechado, name='pedido_fechado')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)