# Generated by Django 4.2.9 on 2024-01-20 00:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('membros', '0008_alter_paciente_tratamento'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paciente',
            name='status',
            field=models.CharField(choices=[('Na fila!', 'Na fila!'), ('Em andamento!', 'Em andamento!'), ('Finalizado!', 'Finalizado')], default='Na fila!', max_length=255, null=True),
        ),
    ]
