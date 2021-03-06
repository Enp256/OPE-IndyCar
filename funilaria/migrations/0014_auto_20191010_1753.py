# Generated by Django 2.2 on 2019-10-10 20:53

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('funilaria', '0013_auto_20191010_1730'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orcamento',
            name='carrinho',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='funilaria.Carrinho'),
        ),
        migrations.AlterField(
            model_name='orcamento',
            name='data_saida',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='orcamento',
            name='ordem_servico',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='funilaria.OrdemDeServico'),
        ),
        migrations.AlterField(
            model_name='orcamento',
            name='previsao_entrega',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='orcamento',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='ordemdeservico',
            name='prazo_entrega',
            field=models.DateField(default=datetime.datetime(2019, 10, 10, 17, 52, 51, 509739)),
        ),
    ]
