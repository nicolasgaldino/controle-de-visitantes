# Generated by Django 4.2.1 on 2023-05-31 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('visitantes', '0002_alter_visitante_cpf'),
    ]

    operations = [
        migrations.AlterField(
            model_name='visitante',
            name='cpf',
            field=models.CharField(max_length=11, verbose_name='CPF'),
        ),
    ]