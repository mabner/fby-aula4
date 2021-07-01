from rest_framework import serializers
from .models.pessoa import Pessoa
from .models import *

class PessoaSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Pessoa
		fields = ('id', 'nome', 'sobrenome')


class DepartamentoSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Departamento
		fields = ('id','nome','numero_sala')


class TelefoneSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Telefone
		fields = ('id', 'ddd', 'numero', 'temWhatsapp')


class PlantaoSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Plantao
		fields = ('id', 'nome', 'horario')


class CargoSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Cargo
		fields = ('id', 'nome', 'nivel')
