from django.contrib import admin
from .models import (
    Marca,
    Veiculo,
    Pessoa,
    Parametro,
    MovRotativo,
    Mensalista,
    MovMensalista
)

class MovRotativoAdmin(admin.ModelAdmin):
    list_display = (
        'checkin', 'checkout', 'valor_hora', 'veiculo', 'pago', 'total',
        'horas_total', 'veiculo') #, teste)

    # Exemplo de possibilildade de como passar alguma informação
    # qualquer como obj para o display do Admin.
    #def teste(self, obj):
    #    return ´Olá´

class MovMensalistaAdmin(admin.ModelAdmin):
    list_display = ('mensalista', 'dt_pgto', 'total')

admin.site.register(Marca)
admin.site.register(Veiculo)
admin.site.register(Pessoa)
admin.site.register(Parametro)
admin.site.register(Mensalista)
admin.site.register(MovMensalista, MovMensalistaAdmin)
admin.site.register(MovRotativo, MovRotativoAdmin)