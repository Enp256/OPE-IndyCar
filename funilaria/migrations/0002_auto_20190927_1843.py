# Generated by Django 2.1.3 on 2019-09-27 21:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('funilaria', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordemdeservico',
            name='cidade_veiculo',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='ordemdeservico',
            name='cor_veiculo',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='ordemdeservico',
            name='marca_veiculo',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='ordemdeservico',
            name='modelo_veiculo',
            field=models.CharField(max_length=30),
        ),
    ]
