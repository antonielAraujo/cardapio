from django.db import models
from datetime import datetime

# Create your models here.

class Categoria(models.Model):
    nome = models.CharField(max_length=100)
    def __str__(self):
        return self.nome

class Comida(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.CharField(max_length=300)
    preco = models.DecimalField(max_digits=5, decimal_places=2)
    estoque = models.IntegerField()
    imagem = models.ImageField(upload_to='imagens/')
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

class Pedido(models.Model):
    data = models.DateTimeField(default=datetime)
    pagamento = models.CharField(max_length=1)

class ComidasPedidos(models.Model):
    comida = models.ForeignKey(Comida, on_delete=models.CASCADE)
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    quantidade = models.IntegerField()