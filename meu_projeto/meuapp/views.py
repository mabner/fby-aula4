from rest_framework import viewsets
from .serializers import PessoaSerializer, DepartamentoSerializer
from .models.pessoa import Pessoa
from .models import Departamento


class PessoaViewSet(viewsets.ModelViewSet):
	queryset = Pessoa.objects.all().order_by('nome')
	serializer_class = PessoaSerializer


class DepartamentoViewSet(viewsets.ModelViewSet):
	queryset = Departamento.objects.all()
	serializer_class = DepartamentoSerializer
