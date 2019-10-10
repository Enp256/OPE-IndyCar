# Generated by Django 2.2 on 2019-10-10 20:30

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('funilaria', '0012_auto_20191010_1703'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='material',
            name='slug',
        ),
        migrations.AlterField(
            model_name='orcamento',
            name='total_a_pagar',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=8),
        ),
        migrations.AlterField(
            model_name='ordemdeservico',
            name='prazo_entrega',
            field=models.DateField(default=datetime.datetime(2019, 10, 10, 17, 30, 44, 921088)),
        ),
    ]
