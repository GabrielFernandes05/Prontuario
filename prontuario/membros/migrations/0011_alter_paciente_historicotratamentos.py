# Generated by Django 4.2.9 on 2024-01-20 03:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('membros', '0010_alter_paciente_historicotratamentos'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paciente',
            name='historicoTratamentos',
            field=models.JSONField(default=dict, null=True),
        ),
    ]