# Generated by Django 4.2.11 on 2024-03-10 12:54

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("anos_letivos", "0005_alter_anoletivo_nome"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="anoletivo",
            name="trimestre",
        ),
    ]
