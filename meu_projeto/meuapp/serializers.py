from rest_framework import serializers
from .models.pessoa import Pessoa
from .models import Departamento

class PessoaSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Pessoa
		fields = ('id','nome','sobrenome','dataNascimento')


class DepartamentoSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Departamento
		fields = ('id','nome','numero_sala')