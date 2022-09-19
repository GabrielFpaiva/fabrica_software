from tkinter import CASCADE
from django.db import models


class categoria(models.Model):
    nome = models.CharField(max_length=100)
    dt_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome

class produto(models.Model):
    data = models.DateTimeField()
    nome = models.CharField(max_length=200)
    valor = models.DecimalField(max_digits=7,decimal_places=2)
    categoria = models.ForeignKey(categoria,on_delete=models.CASCADE)
    obs = models.TextField(null=True,blank=True)

    def __str__(self):
        return self.nome