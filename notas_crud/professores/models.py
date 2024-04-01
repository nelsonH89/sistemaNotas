from django.db import models

# Create your models here.

class Professor(models.Model):
    nome = models.CharField(max_length=80, verbose_name="Nome")
    disc=models.CharField(max_length=30, null=True, verbose_name="Disciplina")
    data_de_nasc = models.DateField( null=True, verbose_name="Data de nascimento")
    telef = models.CharField(max_length=15, blank=True, null=True, verbose_name="Telefone")
    email = models.CharField(max_length=30, blank=True, null=True, verbose_name="Email")

    def __str__(self):
        return self.nome