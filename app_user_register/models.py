from django.db import models

class FormEntry(models.Model):
    client = models.CharField(max_length=100)
    telefone = models.CharField(max_length=15)
    carro = models.CharField(max_length=50)
    cor = models.CharField(max_length=20)
    placa = models.CharField(max_length=10)
    observacao = models.TextField()

    def __str__(self):
        return self.client

