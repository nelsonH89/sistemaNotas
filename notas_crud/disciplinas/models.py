from django.db import models

from professores.models import Professor

# Create your models here.

class Disciplina(models.Model):
    nome=models.CharField(max_length=30)
    cargaHo=models.CharField(max_length=5, blank=True, null=True)
    professor=models.ForeignKey('professores.Professor', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.nome
    