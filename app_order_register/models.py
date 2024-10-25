from django.db import models

class Order(models.Model):
    client = models.CharField(max_length=255)
    telefone = models.CharField(max_length=20)
    carro = models.CharField(max_length=100)
    cor = models.CharField(max_length=50)
    placa = models.CharField(max_length=10)
    observacao = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Order {self.id} - {self.client}"


