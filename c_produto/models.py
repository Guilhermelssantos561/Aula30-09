from django.db import models

class Produto(models.Model):
    nome = models.CharField(max_length=100)
    estoque = models.IntegerField()
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    foto_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.nome
