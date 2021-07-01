from django.db import models


class Plantao(models.Model):
    nome = models.CharField(max_length=20, default="Normal")
    horario = models.CharField(max_length=10, null=True)

    def __str__(self):
        return self.nome
