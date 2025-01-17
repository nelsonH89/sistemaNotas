# Generated by Django 5.0.3 on 2024-03-06 22:19

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("trimestres", "0003_alter_trimestre_trimestre"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="trimestre",
            name="anoletivo",
        ),
        migrations.RemoveField(
            model_name="trimestre",
            name="fimT",
        ),
        migrations.RemoveField(
            model_name="trimestre",
            name="inicioT",
        ),
        migrations.AlterField(
            model_name="trimestre",
            name="trimestre",
            field=models.CharField(
                choices=[
                    ("1ºTrimestre", "1ºTrimestre"),
                    ("2ºTrimestre", "2ºTrimestre"),
                    ("3ºTrimestre", "3ºTrimestre"),
                    ("Exame", "Exame"),
                    ("Recurso", "Recurso"),
                ],
                max_length=15,
                null=True,
            ),
        ),
    ]
