from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Pessoa, Telefone
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
import json


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
@require_http_methods(['GET', 'POST'])
def listar_com_parametro(request):

    _idade = request.POST['idade']
    pessoas = Pessoa.objects.filter(idade__exact=_idade)
    pessoas_json = []

    for pessoa in pessoas:
        pdic = {
            'nome': pessoa.nome, 'sobrenome': pessoa.sobrenome,
            'idade': pessoa.idade
        }
        pessoas_json.append(pdic)

    payload = {
        'pessoas': pessoas_json
    }

    return JsonResponse(payload)


@csrf_exempt
@require_http_methods(['GET', 'POST'])
def listar_pessoas(request):

    pessoas = Pessoa.objects.all()
    pessoas_json = []

    for pessoa in pessoas:
        pdic = {
            'id': pessoa.id,
            'nome': pessoa.nome, 'sobrenome': pessoa.sobrenome,
            'idade': pessoa.idade
        }
        pessoas_json.append(pdic)

    payload = {
        'pessoas': pessoas_json
    }

    return JsonResponse(payload)


def detalhar_pessoa(request, idpessoa):

    pessoa = Pessoa.objects.obter_pessoa_id(idpessoa)
    payload = {
        'nome': pessoa.nome,
        'sobrenome': pessoa.sobrenome
    }

    return JsonResponse(payload)


def indice(request):

    response = HttpResponse()

    if request.method == 'GET':
        response.write("Usei o método GET")
    elif request.method == 'POST':
        response.write("Usei o método POST")

    return response


def detalhar_pessoa2(request, idpessoa):

    # Verificar se os parâmetros são válidos
    try:
        pessoa = Pessoa.objects.obter_pessoa_id(idpessoa)
    except:
        return HttpResponse("Erro ao buscar Pessoa")

    return HttpResponse(f"Você procurou a pessoa de nome {pessoa.nome}")


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
