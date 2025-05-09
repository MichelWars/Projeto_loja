from django.db import models
from produtos.models import Produto



class Entrada(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.PROTECT, related_name='entradas')
    quantidade = models.IntegerField()
    data_entrada = models.DateTimeField(auto_now_add=True)


    # ordenação por registros mais recentes
    class Meta:
        ordering = ['-data_entrada']

    # caso a tabela não tenho registro sera retornado um objeto nulo convertido em string para evitar erros
    def __str__(self):
        return str(self.produto)
