from django.db import models

# Create your models here.
class Pessoa(models.Model):
    nome = models.CharField(max_length=100)
    # Troca a visualização do pessoa object para o nome da pessoa
    def __str__(self):
        return self.nome
    