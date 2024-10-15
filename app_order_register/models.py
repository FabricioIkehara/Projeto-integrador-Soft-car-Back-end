from django.db import models
from djongo import models

class FormEntry(models.Model):
    client = models.CharField(max_length=100)  
    telefone = models.CharField(max_length=15)  
    carro= models.CharField(max_length=50)
    cor = models.CharField(max_length=50)  
    placa = models.CharField(max_length=8)  
    observacoes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.client} - {self.carro}"