from django.contrib import admin

from .models import Entrada


class EntradaAdmin(admin.ModelAdmin):
    list_display = ('produto', 'quantidade', 'data_entrada')


admin.site.register(Entrada, EntradaAdmin)
