# Generated by Django 5.0.3 on 2024-03-06 22:19

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("professores", "0002_remove_professor_idade_professor_data_de_nasc_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="professor",
            old_name="disciplina",
            new_name="disc",
        ),
    ]
