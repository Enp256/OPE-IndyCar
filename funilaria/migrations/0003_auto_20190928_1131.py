# Generated by Django 2.1.3 on 2019-09-28 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('funilaria', '0002_auto_20190927_1843'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='cpf',
            field=models.CharField(max_length=14),
        ),
        migrations.AlterField(
            model_name='customer',
            name='telefone',
            field=models.CharField(max_length=15),
        ),
        migrations.AlterField(
            model_name='empresa',
            name='cnpj',
            field=models.CharField(max_length=18),
        ),
        migrations.AlterField(
            model_name='material',
            name='valor',
            field=models.CharField(max_length=14),
        ),
        migrations.AlterField(
            model_name='ordemdeservico',
            name='placa_veiculo',
            field=models.CharField(max_length=8),
        ),
    ]
