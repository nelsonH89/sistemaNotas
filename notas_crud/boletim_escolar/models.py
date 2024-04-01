from django.db import models

from alunos.models import Aluno
from notas.models import Nota
from trimestres.models import Trimestre

# Create your models here.
class Boletim(models.Model):
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    trimestre = models.ForeignKey(Trimestre, on_delete=models.CASCADE)
    notas = models.ManyToManyField(Nota)