from django.http import HttpResponse
from django.http.response import JsonResponse
from django.template import loader
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from rest_framework import viewsets
from .serializers import *
from .models.pessoa import Pessoa
from .models import *
import json


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


@csrf_exempt
@require_http_methods(['GET', 'POST'])
def enviar_json(request):

    payload = json.loads(request.body)

    """
	{
	    "nome_completo": "Marcos Leite",
	    "telefone": {
	        "ddd":31,
	        "numero":"912345678"
	    }
	}
	"""

    _nome_completo = payload["nome_completo"]
    _nome = _nome_completo.split(" ")[0]
    _sobrenome = _nome_completo.split(" ")[1]
    _ddd = payload["telefone"]["ddd"]
    _numero = payload["telefone"]["numero"]

    try:
        # Métodos para salvar as informações
        pessoa = Pessoa(nome=_nome, sobrenome=_sobrenome)
        pessoa.save()

        tel = Telefone(ddd=_ddd, numero=_numero, temWhatsapp=False)
        tel.save()

        pessoa.telefones.add(tel)

        # Mensagem de confirmação do cadastro
        mensagem = f"Dados de {_nome} cadastrados com sucesso!"

    except Exception as error:
        mensagem = f"Falha ao cadastrar: {error}"

    return JsonResponse({"mensagem": mensagem})


@csrf_exempt
def detalharpessoa(request):

    pessoas = Pessoa.objects.order_by('nome')
    template = loader.get_template('pessoa/detalhar.html')
    context = {
        'listapessoas': pessoas,
    }
    return HttpResponse(template.render(context, request))


@csrf_exempt
def listar_pessoas(request):

    pessoas = Pessoa.objects.all()
    lista = {"listarpessoas": pessoas}

    for pessoa in pessoas:
        pdic = {
            'id': pessoa.id,
            'nome': pessoa.nome, 'sobrenome': pessoa.sobrenome,
            'idade': pessoa.idade
        }
        lista[pessoas] = pdic

    template = loader.get_template("pessoa/index.html")

    return HttpResponse(template.render(lista, request))


@csrf_exempt
def apagar(request, idpessoa):
    try:
        Pessoa.objects.get(id=idpessoa).delete()
    except:
        return HttpResponse("Erro ao apagar a pessoa, ou não encontrada")

    return HttpResponse("Pessoa apagada")


@csrf_exempt
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
