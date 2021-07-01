from django.contrib import admin
from .models import *
from .models.pessoa import Pessoa

# Register your models here.
admin.site.register(Pessoa)
admin.site.register(Departamento)
admin.site.register(Telefone)
admin.site.register(Plantao)
admin.site.register(Cargo)
