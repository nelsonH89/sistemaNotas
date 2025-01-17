# Generated by Django 4.2.11 on 2024-03-14 07:01

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("notas", "0004_remove_nota_nome_aluno_nota_aluno_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="nota",
            name="mac",
            field=models.FloatField(
                validators=[
                    django.core.validators.MinValueValidator(0),
                    django.core.validators.MaxValueValidator(20),
                ]
            ),
        ),
        migrations.AlterField(
            model_name="nota",
            name="np",
            field=models.FloatField(
                validators=[
                    django.core.validators.MinValueValidator(0),
                    django.core.validators.MaxValueValidator(20),
                ]
            ),
        ),
        migrations.AlterField(
            model_name="nota",
            name="nt",
            field=models.FloatField(
                validators=[
                    django.core.validators.MinValueValidator(0),
                    django.core.validators.MaxValueValidator(20),
                ]
            ),
        ),
    ]
