# Generated by Django 2.2 on 2019-10-05 17:51

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('funilaria', '0002_auto_20191005_1451'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordemdeservico',
            name='prazo_entrega',
            field=models.DateField(default=datetime.datetime(2019, 10, 5, 14, 51, 58, 830008)),
        ),
    ]
