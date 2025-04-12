from django.db.models.signals import pre_save
from django.dispatch import receiver
from .models import Cliente


# Signal para formatar o nome e sobrenome antes de salvar o cliente
@receiver(pre_save, sender=Cliente)
def formatar_nome_sobrenome(sender, instance, **kwargs):
    if instance.nome:
        instance.nome = ' '.join(p.capitalize() for p in instance.nome.split())
    if instance.sobrenome:
        instance.sobrenome = ' '.join(p.capitalize() for p in instance.sobrenome.split())
