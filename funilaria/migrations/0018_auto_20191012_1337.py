# Generated by Django 2.2 on 2019-10-12 16:37

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('funilaria', '0017_auto_20191012_1247'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itemcarrinho',
            name='quantidade',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='ordemdeservico',
            name='prazo_entrega',
            field=models.DateField(default=datetime.datetime(2019, 10, 12, 13, 37, 40, 591536)),
        ),
    ]
