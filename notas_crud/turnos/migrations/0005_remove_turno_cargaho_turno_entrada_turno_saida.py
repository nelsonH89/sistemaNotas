# Generated by Django 5.0.3 on 2024-03-06 21:13

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("turnos", "0004_remove_turno_entrada_remove_turno_saida_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="turno",
            name="cargaHo",
        ),
        migrations.AddField(
            model_name="turno",
            name="entrada",
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AddField(
            model_name="turno",
            name="saida",
            field=models.CharField(max_length=15, null=True),
        ),
    ]
