# Generated by Django 5.0.3 on 2024-03-06 19:28

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("professores", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="professor",
            name="idade",
        ),
        migrations.AddField(
            model_name="professor",
            name="data_de_nasc",
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name="professor",
            name="disciplina",
            field=models.CharField(max_length=30, null=True),
        ),
    ]