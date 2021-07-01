from django.urls import include, path
from rest_framework import routers
from . import views


router = routers.DefaultRouter()
router.register(r'pessoas', views.PessoaViewSet)
router.register(r'departamento', views.DepartamentoViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/',
         include('rest_framework.urls',
                 namespace='rest_framework')
         )
]

# Backup dos paths

# urlpatterns = [
#     path('', views.indice, name='indice'),
#     path('pessoa/<int:idpessoa>', views.detalhar_pessoa, name='detalhar_pessoa'),
#     path('pessoa/listar', views.listar_pessoas, name='listar'),
#     path('pessoa/listar_com_parametro',
#          views.listar_com_parametro, name='listar_com_parametro'),
#     path('pessoa2/<int:idpessoa>', views.detalhar_pessoa2, name='detalhar_pessoa2'),
#     path('enviar_json', views.enviar_json, name='enviar_json'),
#     path('pessoa/apagar/<int:idpessoa>',
#          views.apagar, name="pessoa_apagada"),
#     path('pessoa/editar/<int:idpessoa>',
#          views.editar_pessoa, name="editar_pessoa")
# ]
