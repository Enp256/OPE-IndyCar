# Generated by Django 2.2 on 2019-10-10 19:55

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('funilaria', '0008_auto_20191009_0904'),
    ]

    operations = [
        migrations.AddField(
            model_name='orcamento',
            name='finalizado',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='ordemdeservico',
            name='prazo_entrega',
            field=models.DateField(default=datetime.datetime(2019, 10, 10, 16, 55, 5, 539559)),
        ),
    ]
