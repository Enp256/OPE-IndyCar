# Generated by Django 2.2.5 on 2019-09-19 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('funilaria', '0002_auto_20190919_1016'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordemdeservico',
            name='entrada',
            field=models.DateField(auto_now_add=True),
        ),
    ]
