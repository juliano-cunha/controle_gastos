from django.db import models


class Categoria(models.Model):
    """Classe para as categorias de gastos herdando da classe de models django"""
    nome = models.CharField(max_length=100)
    dt_criacao = models.DateField(auto_now_add=True)

    def __str__(self):
        """Funcao que corrige o nome mostrado no admin da categoria, não apenas o object"""
        return self.nome


class Transacao(models.Model):
    """Classe para as transações do programa"""
    data = models.DateTimeField()
    descricao = models.CharField(max_length=200)
    valor = models.DecimalField(max_digits=7, decimal_places=2)
    # relacionamento do campo com o banco e outra classe
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    observacoes = models.TextField(null=True, blank=True)

    class Meta:
        """utiliza a meta classe para corrigir o nome no plural, django docs """
        verbose_name_plural = 'Transações'

    def __str__(self):
        """Funcao que corrige o nome mostrado no admin"""
        return self.descricao
