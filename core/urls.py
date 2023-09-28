from django.urls import path
from .views import *
urlpatterns = [
    path('', home, name='home'),
    path('cad_categoria/', cad_categoria, name='cad_categoria')
]