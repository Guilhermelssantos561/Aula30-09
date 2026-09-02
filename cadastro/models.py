from django.db import models

class Usuario(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    perfil = models.CharField(max_length=50)

    def __str__(self):
        return self.nome
