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
