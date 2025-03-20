from django.db import models


# Essa choice fornece opções fixas de itens para o campo CONSOLE
CONSOLE_CHOICES = (
    ('PS4', 'Playstation 4'),
    ('PS5', 'Playstation 5'),
    ('XBOX', 'Xbox One'),
    ('XBOX-S', 'Xbox Series X'),
    ('SWITCH', 'Nintendo Switch'),
)


# Essa classe representa produtos no banco de dados
class Produto(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=200)
    console = models.CharField(
        max_length=100,
        choices=CONSOLE_CHOICES,
        blank=True,
        null=True,
    )
    ano_lancamento = models.IntegerField(blank=True, null=True)
    valor = models.FloatField(blank=True, null=True)
    foto = models.ImageField(upload_to='produtos/', blank=True, null=True)
    descricao = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.titulo


# Essa classe representa o inventário de produtos
class ProdutoInventory(models.Model):
    produto_count = models.IntegerField()
    produto_value = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.produto_count} - {self.produto_value}'
