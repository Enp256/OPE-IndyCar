# Generated by Django 2.2.2 on 2019-09-18 17:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=60)),
                ('endereco', models.CharField(max_length=100)),
                ('bairro', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=60)),
                ('telefone', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Orcamento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantidade', models.IntegerField()),
                ('pecas', models.TextField(max_length=200)),
                ('servicos', models.TextField(max_length=500)),
                ('valor_mao_de_obra', models.FloatField()),
                ('previsao_entrega', models.DateField()),
                ('data_saida', models.DateField()),
                ('total_a_pagar', models.DecimalField(decimal_places=2, max_digits=8)),
            ],
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('customer_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='funilaria.Customer')),
                ('rg', models.IntegerField()),
            ],
            bases=('funilaria.customer',),
        ),
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('customer_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='funilaria.Customer')),
                ('cnpj', models.CharField(max_length=14)),
            ],
            bases=('funilaria.customer',),
        ),
        migrations.CreateModel(
            name='OrdemDeServico',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marca_veiculo', models.CharField(max_length=10)),
                ('modelo_veiculo', models.CharField(max_length=20)),
                ('cor_veiculo', models.CharField(max_length=10)),
                ('ano_veiculo', models.SmallIntegerField()),
                ('placa_veiculo', models.CharField(max_length=7)),
                ('cidade_veiculo', models.CharField(max_length=10)),
                ('estado_veiculo', models.CharField(max_length=2)),
                ('reparos_necessarios', models.TextField(max_length=200)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='funilaria.Customer')),
            ],
        ),
    ]
