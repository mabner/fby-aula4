from django.urls import include, path
from rest_framework import routers
from . import views


router = routers.DefaultRouter()
router.register(r'pessoas', views.PessoaViewSet)
router.register(r'departamento', views.DepartamentoViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('pessoa/<int:idpessoa>', views.detalharpessoa, name='detalhar_pessoa'),
    path('pessoa/listar', views.listar_pessoas, name='listar'),
    path('pessoa', views.pessoa, name='index'),
    path('pessoa/apagar/<int:idpessoa>',
         views.apagar, name="pessoa_apagada"),
    path('pessoa/editar/<int:idpessoa>',
         views.editar_pessoa, name="editar_pessoa")
]
