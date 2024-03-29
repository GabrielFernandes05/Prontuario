# Generated by Django 4.2.9 on 2024-01-19 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('membros', '0005_paciente_doente_delete_customuser'),
    ]

    operations = [
        migrations.AddField(
            model_name='paciente',
            name='status',
            field=models.CharField(choices=[('Na fila!', 'Na fila!'), ('Finalizado!', 'Finalizado'), ('Em andamento!', 'Em andamento!')], max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='paciente',
            name='tratamento',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
