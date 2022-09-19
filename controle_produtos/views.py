from django.shortcuts import render,redirect
from .models import produto
from .form import produtoForm


def lista_produto(request):
    data = {}
    data['produtos'] = produto.objects.all()
    return render(request, 'controle_produtos/lista.html',data)

def novo_produto(request):
    data = {}
    form = produtoForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('lista')
    
    data['form'] = form

    return render(request,'controle_produtos/cadastro.html',data)
