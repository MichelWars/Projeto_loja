from django.contrib import admin
from .models import Cliente

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'sobrenome', 'cpf', 'telefone', 'data_nascimento', 'email_do_usuario')
    search_fields = ('nome', 'sobrenome', 'cpf', 'user__email')

    def email_do_usuario(self, obj):
        return obj.user.email
    email_do_usuario.short_description = 'E-mail'  # Nome da coluna no admin
