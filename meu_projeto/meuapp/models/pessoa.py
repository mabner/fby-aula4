from django.db import models
from . import Departamento, Telefone, Cargo, Plantao


class PessoaManager(models.Manager):

    def obter_pessoa_id(self, idpessoa):
        return self.get(id=idpessoa)

    def obter_todas_pessoas(self):
        return self.all()

    def obter_familia(self):
        pessoas = self.filter(sobrenome="Leite")
        return pessoas

    def obter_masculino(self):
        masculino = self.filter(sexo="M")
        return masculino

    def obter_feminino(self):
        feminino = self.filter(sexo="F")
        return feminino

    def obter_maioridade(self):
        maiores = self.filter(idade__gte=18)
        # gte -> greater than or equal to
        return maiores

    def obter_primeiro_cadastro(self):
        primeiro = self.get(id=1)
        return primeiro

    def pessoas_m(self):
        pessoas_m = self.filter(nome__startswith="M")
        return pessoas_m

    def create_pessoa(self, nome_completo):
        _nome_completo = nome_completo.split(" ")
        pessoa = self.create(nome=_nome_completo[0],
                             sobrenome=_nome_completo[1])
        return pessoa


class Pessoa(models.Model):
    SEXO_CHOICES = [('M', 'Masculino'),
                    ('F', 'Feminino')]

    nome = models.CharField(max_length=50)

    sobrenome = models.CharField(max_length=50,
                                 null=True)
    idade = models.IntegerField(default=0)

    sexo = models.CharField(max_length=10,
                            choices=SEXO_CHOICES,
                            default='M')

    departamento = models.ForeignKey(Departamento,
                                     on_delete=models.SET_NULL,
                                     null=True)

    cargo = models.ForeignKey(Cargo, on_delete=models.SET_NULL,
                              null=True)

    plantao = models.ForeignKey(Plantao, on_delete=models.SET_NULL,
                                null=True)

    telefones = models.ManyToManyField(Telefone)

    objects = PessoaManager()

    def __str__(self):
        return f"{self.nome} {self.sobrenome}"
