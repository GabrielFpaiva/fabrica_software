from django.shortcuts import render
from .models import produto


def home(request):
    data = {}
    data['produtos'] = produto.objects.all()
    return render(request, 'controle_produtos/home.html',data)
