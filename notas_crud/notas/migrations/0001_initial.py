# Generated by Django 5.0.3 on 2024-03-05 05:43

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Nota",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nome_aluno", models.CharField(max_length=80)),
                ("trimestre", models.CharField(max_length=15)),
                ("mac", models.DecimalField(decimal_places=1, max_digits=4)),
                ("np", models.DecimalField(decimal_places=1, max_digits=4)),
                ("nt", models.DecimalField(decimal_places=1, max_digits=4)),
            ],
        ),
    ]
