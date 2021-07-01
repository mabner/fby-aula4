from django.http import HttpResponse
from django.template import loader
from rest_framework import viewsets
from .serializers import *
from .models.pessoa import Pessoa
from .models import *


class PessoaViewSet(viewsets.ModelViewSet):
    queryset = Pessoa.objects.all().order_by('nome')
    serializer_class = PessoaSerializer


class DepartamentoViewSet(viewsets.ModelViewSet):
    queryset = Departamento.objects.all()
    serializer_class = DepartamentoSerializer


class TelefoneViewSet(viewsets.ModelViewSet):
    queryset = Telefone.objects.all()
    serializer_class = TelefoneSerializer


class PlantaoViewSet(viewsets.ModelViewSet):
    queryset = Plantao.objects.all()
    serializer_class = PlantaoSerializer


class CargoViewSet(viewsets.ModelViewSet):
    queryset = Cargo.objects.all()
    serializer_class = CargoSerializer


def detalharpessoa(request):

    pessoas = Pessoa.objects.order_by('nome')
    template = loader.get_template('pessoa/detalhar.html')
    context = {
        'listapessoas': pessoas,
    }
    return HttpResponse(template.render(context, request))


def listar_pessoas(request):

    pessoas = Pessoa.objects.all()
    lista = {"listarpessoas": pessoas}

    for pessoa in pessoas:
        pdic = {
            'id': pessoa.id,
            'nome': pessoa.nome, 'sobrenome': pessoa.sobrenome,
            'idade': pessoa.idade
        }
        lista.append(pdic)

    template = loader.get_template("pessoa/listar.html")

    return HttpResponse(template.render(lista, request))


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
