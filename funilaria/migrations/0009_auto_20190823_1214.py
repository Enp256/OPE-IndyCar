# Generated by Django 2.2.2 on 2019-08-23 15:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('funilaria', '0008_auto_20190823_1145'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='veiculo',
            name='entrada',
        ),
        migrations.RemoveField(
            model_name='veiculo',
            name='finalizado',
        ),
    ]