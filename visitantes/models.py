from django.db import models


class Visitante(models.Model):
    nome_completo = models.CharField(
        verbose_name='Nome completo',
        max_length=194,
    )
    cpf = models.CharField(
        verbose_name='CFP',
        unique=True,
        max_length=11,
    )
    data_nascimento = models.DateField(
        verbose_name='Data de Nascimento',
        auto_now=False,
        auto_now_add=False,
    )
    numero_casa = models.PositiveSmallIntegerField(
        verbose_name='Número da casa a ser visitada'
    )
    placa_veiculo = models.CharField(
        verbose_name='Placa do veículo',
        max_length=7,
        blank=True,
        null=True,
    )
    horario_chegada = models.DateTimeField(
        verbose_name='Horário de chegada na portaria',
        auto_now_add=True,
    )
    horario_saida = models.DateTimeField(
        verbose_name='Horário de saída do condomínio',
        auto_now=False,
        blank=True,
        null=True,
    )
    horario_autorizacao = models.DateTimeField(
        verbose_name='Horário de autorização de entrada',
        auto_now=False,
        blank=True,
        null=True,
    )
    morador_responsavel = models.CharField(
        verbose_name='Morador responsável por autorizar a entrada',
        max_length=194,
        blank=True,
    )
