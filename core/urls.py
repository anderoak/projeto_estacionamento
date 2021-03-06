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
    movmensalistas_delete,
    pessoa_exporta_pdf,
    pessoa_exporta_csv,
    veiculo_exporta_pdf,
    veiculo_exporta_csv,
    mensalista_exporta_pdf,
    mensalista_exporta_csv,
    movrotativo_exporta_pdf,
    movrotativo_exporta_csv,
    movmensalista_exporta_pdf,
    movmensalista_exporta_csv
)

urlpatterns = [
    path('', home, name='home'),
    
    path('pessoas', lista_pessoas, name='core_lista_pessoas'),
    path('pessoa_novo', pessoa_novo, name='core_pessoa_novo'),
    path('pessoa_update/<int:id>/', pessoa_update, name='core_pessoa_update'),
    path('pessoa_delete/<int:id>/', pessoa_delete, name='core_pessoa_delete'),

    path('pessoa_relatorio', pessoa_exporta_pdf.as_view(), name='pessoa_relatorio_pdf'),
    path('pessoa_relatorio_csv', pessoa_exporta_csv.as_view(), name='pessoa_relatorio_csv'),

    path('veiculos', lista_veiculos, name='core_lista_veiculos'),
    path('veiculo_novo', veiculo_novo, name='core_veiculo_novo'),
    path('veiculo_update/<int:id>/', veiculo_update, name='core_veiculo_update'),
    path('veiculo_delete/<int:id>/', veiculo_delete, name='core_veiculo_delete'),

    path('veiculo_relatorio', veiculo_exporta_pdf.as_view(), name='veiculo_relatorio_pdf'),
    path('veiculo_relatorio_csv', veiculo_exporta_csv.as_view(), name='veiculo_relatorio_csv'),
    
    path('mensalistas', lista_mensalistas, name='core_lista_mensalistas'),
    path('mensalista_novo', mensalista_novo, name='core_mensalista_novo'),
    path('mensalista_update/<int:id>/', mensalista_update, name='core_mensalista_update'),
    path('mensalista_delete/<int:id>/', mensalista_delete, name='core_mensalista_delete'),

    path('mensalista_relatorio', mensalista_exporta_pdf.as_view(), name='mensalista_relatorio_pdf'),
    path('mensalista_relatorio_csv', mensalista_exporta_csv.as_view(), name='mensalista_relatorio_csv'),

    path('movrotativos', lista_movrotativos, name='core_lista_movrotativos'),
    path('movrotativos_novo', movrotativos_novo, name='core_movrotativos_novo'),
    path('movrotativos_update/<int:id>/', movrotativos_update, name='core_movrotativos_update'),
    path('movrotativos_delete/<int:id>/', movrotativos_delete, name='core_movrotativos_delete'),

    path('movrotativo_relatorio', movrotativo_exporta_pdf.as_view(), name='movrotativo_relatorio_pdf'),
    path('movrotativo_relatorio_csv', movrotativo_exporta_csv.as_view(), name='movrotativo_relatorio_csv'),

    path('movmensalistas', lista_movmensalistas, name='core_lista_movmensalistas'),
    path('movmensalistas_novo', movmensalistas_novo, name='core_movmensalistas_novo'),
    path('movmensalistas_update/<int:id>/', movmensalistas_update, name='core_movmensalistas_update'),
    path('movmensalistas_delete/<int:id>/', movmensalistas_delete, name='core_movmensalistas_delete'),

    path('movmensalista_relatorio', movmensalista_exporta_pdf.as_view(), name='movmensalista_relatorio_pdf'),
    path('movmensalista_relatorio_csv', movmensalista_exporta_csv.as_view(), name='movmensalista_relatorio_csv'),

]
