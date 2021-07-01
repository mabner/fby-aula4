from django.db import models


class Departamento(models.Model):
    nome = models.CharField(max_length=50)
    numero_sala = models.IntegerField(default=0)

    def __str__(self):
        return self.nome
