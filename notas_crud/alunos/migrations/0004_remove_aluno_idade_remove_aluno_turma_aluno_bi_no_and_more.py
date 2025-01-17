# Generated by Django 5.0.3 on 2024-03-06 18:50

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("alunos", "0003_alter_aluno_turma"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="aluno",
            name="idade",
        ),
        migrations.RemoveField(
            model_name="aluno",
            name="turma",
        ),
        migrations.AddField(
            model_name="aluno",
            name="BI_No",
            field=models.CharField(max_length=14, null=True, unique=True),
        ),
        migrations.AddField(
            model_name="aluno",
            name="data_de_nascimento",
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name="aluno",
            name="email",
            field=models.EmailField(blank=True, max_length=40, null=True),
        ),
        migrations.AddField(
            model_name="aluno",
            name="telefone",
            field=models.CharField(blank=True, max_length=17, null=True, unique=True),
        ),
    ]
