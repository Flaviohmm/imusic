from django.urls import path
from . import views

app_name = 'plataforma'
urlpatterns = [
    # home /
    path('', views.home, name="home"),

    # detalhe_perfil /@username/
    path('@<str:username>/', views.detalhe_perfil, name="detalhe_perfil"),

    # adicionar novo álbum /@username/adicionar
    path('@<str:username>/adicionar/', views.adicionar_album, name="adicionar_album"),

    # página de detalhes do álbum /@username/album/nome_do_album
    path('@<str:username>/album/<str:album>/', views.detalhe_album, name="detalhe_album"),

    # deletar álbum /@username/album/nome_do_album/deletar
    path('@<str:username>/album/<str:album>/deletar/', views.deletar_album, name="deletar_album"),
]