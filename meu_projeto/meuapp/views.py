from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .serializers import *
from .models.pessoa import Pessoa
from .models import *


def index(request):
    return render(request, 'pessoa/index.html')


def listar_pessoas(request):
    pessoas = Pessoa.objects.obter_todas_pessoas()
    return render(request, 'pessoa/listar.html', {'pessoas': pessoas})


def detalharpessoa(request):

    pessoas = Pessoa.objects.order_by('nome')
    template = loader.get_template('pessoa/detalhar.html')
    context = {
        'listapessoas': pessoas,
    }
    return HttpResponse(template.render(context, request))


def pessoa(request):

    template = loader.get_template("pessoa/index.html")
    return HttpResponse(template.render(request))


def apagar(request, idpessoa):
    try:
        Pessoa.objects.get(id=idpessoa).delete()
    except:
        return HttpResponse("Erro ao apagar a pessoa, ou não encontrada")

    return HttpResponse("Pessoa apagada")


def editar_pessoa(request, idPessoa, nome, sobrenome, idade):
    try:
        pessoa = Pessoa.objects.get(id=idPessoa)
        pessoa.nome = nome
        pessoa.sobrenome = sobrenome
        pessoa.idade = idade
        pessoa.save()

    except:
        return HttpResponse("Erro ao editar registro")

    return HttpResponse("Registro atualizado")
