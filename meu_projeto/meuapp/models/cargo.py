from django.db import models


class Cargo(models.Model):
    nome = models.CharField(max_length=40)
    nivel = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.nome} {self.nivel}"
