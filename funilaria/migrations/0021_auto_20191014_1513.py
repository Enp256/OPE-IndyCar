# Generated by Django 2.2 on 2019-10-14 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('funilaria', '0020_auto_20191013_1328'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orcamento',
            name='finalizado',
        ),
        migrations.AlterField(
            model_name='orcamento',
            name='data_saida',
            field=models.DateField(blank=True, null=True),
        ),
    ]
