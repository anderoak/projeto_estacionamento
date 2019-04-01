from django.urls import path, include, re_path
from .views import (
    home,
    lista_pessoas,
    lista_veiculos,
    lista_movrotativos,
    lista_mensalistas,
    lista_movmensalistas,
    pessoa_novo,
    veiculo_novo,
    movrotativos_novo,
    mensalista_novo,
    movmensalistas_novo,
    pessoa_update,
    veiculo_update,
    movrotativos_update,
    mensalista_update,
    movmensalistas_update,
    pessoa_delete,
    veiculo_delete,
    movrotativos_delete,
    mensalista_delete,
    movmensalistas_delete
)

urlpatterns = [
    path('', home, name='core.urls'),
    
    path('pessoas', lista_pessoas, name='core_lista_pessoas'),
    path('pessoa_novo', pessoa_novo, name='core_pessoa_novo'),
    re_path(r'^pessoa_update/(?P<id>\d+)/$', pessoa_update, name='core_pessoa_update'),
    re_path(r'^pessoa_delete/(?P<id>\d+)/$', pessoa_delete, name='core_pessoa_delete'),

    path('veiculos', lista_veiculos, name='core_lista_veiculos'),
    path('veiculo_novo', veiculo_novo, name='core_veiculo_novo'),
    re_path(r'^veiculo_update/(?P<id>\d+)/$', veiculo_update, name='core_veiculo_update'),
    re_path(r'^veiculo_delete/(?P<id>\d+)/$', veiculo_delete, name='core_veiculo_delete'),
    
    path('movrotativos', lista_movrotativos, name='core_lista_movrotativos'),
    path('movrotativos_novo', movrotativos_novo, name='core_movrotativos_novo'),
    re_path(r'^movrotativos_update/(?P<id>\d+)/$', movrotativos_update, name='core_movrotativos_update'),
    re_path(r'^movrotativos_delete/(?P<id>\d+)/$', movrotativos_delete, name='core_movrotativos_delete'),

    path('mensalistas', lista_mensalistas, name='core_lista_mensalistas'),
    path('mensalista_novo', mensalista_novo, name='core_mensalista_novo'),
    re_path(r'^mensalista_update/(?P<id>\d+)/$', mensalista_update, name='core_mensalista_update'),
    re_path(r'^mensalista_delete/(?P<id>\d+)/$', mensalista_delete, name='core_mensalista_delete'),

    path('movmensalistas', lista_movmensalistas, name='core_lista_movmensalistas'),
    path('movmensalistas_novo', movmensalistas_novo, name='core_movmensalistas_novo'),
    re_path(r'^movmensalistas_update/(?P<id>\d+)/$', movmensalistas_update, name='core_movmensalistas_update'),
    re_path(r'^movmensalistas_delete/(?P<id>\d+)/$', movmensalistas_delete, name='core_movmensalistas_delete'),
]
