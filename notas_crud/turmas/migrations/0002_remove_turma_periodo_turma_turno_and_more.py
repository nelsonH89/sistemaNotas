# Generated by Django 5.0.3 on 2024-03-06 20:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("anos_letivos", "0003_alter_anoletivo_fim_alter_anoletivo_inicio"),
        ("turmas", "0001_initial"),
        ("turnos", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="turma",
            name="periodo",
        ),
        migrations.AddField(
            model_name="turma",
            name="turno",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="turnos.turno",
            ),
        ),
        migrations.AlterField(
            model_name="turma",
            name="anoLetivo",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="anos_letivos.anoletivo"
            ),
        ),
        migrations.AlterField(
            model_name="turma",
            name="nome",
            field=models.CharField(max_length=4, unique=True),
        ),
    ]