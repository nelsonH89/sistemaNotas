from django.db import models

from alunos.models import Aluno
from disciplinas.models import Disciplina
from turmas.models import Turma
from trimestres.models import Trimestre

# Create your models here.
from django.core.validators import MinValueValidator, MaxValueValidator

class Nota(models.Model):
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE, null=True)
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE, null=True)
    trimestre = models.ForeignKey(Trimestre, on_delete=models.CASCADE, null=True)
    turma = models.ForeignKey(Turma, on_delete=models.CASCADE, null=True)
    mac = models.FloatField(validators=[MinValueValidator(0), MaxValueValidator(20)])
    np = models.FloatField(validators=[MinValueValidator(0), MaxValueValidator(20)])
    nt = models.FloatField(validators=[MinValueValidator(0), MaxValueValidator(20)])

    class Meta:
        unique_together = ('aluno', 'turma', 'trimestre', 'disciplina')
    #Média trimestral de cada disciplina
    def media(self):
        return round((self.mac+self.np+self.nt)/3,1)
   #Média trimestral de todas disciplina 
    def media_trimestral(self, trimestre):
        notas = Nota.objects.filter(aluno=self, trimestre=trimestre)
        media_trimestral = notas.aggregate(Avg('media'))['media__avg']
        return round(media_trimestral, 1) if media_trimestral else None
    #Média anual
    def media_anual(self, ano):
        notas = Nota.objects.filter(aluno=self, ano_letivo=ano)
        medias = [nota.media() for nota in notas]
        return round(sum(medias) / len(medias), 1) if medias else None
    #Média anual por disciplina
    def media_anual_por_disciplina(self, ano):
        notas = Nota.objects.filter(aluno=self, ano_letivo=ano)
        medias_por_disciplina = notas.values('disciplina').annotate(media_anual=Avg('media'))
        return medias_por_disciplina
    #Média do curso ou de todos os anos letivos
    def media_do_curso(self):
        alunos = Aluno.objects.filter(curso=self)  # obtenha todos os alunos do curso
        medias_anuais = [aluno.media_anual() for aluno in alunos]  # calcule a média anual para cada aluno
        media_do_curso = sum(medias_anuais) / len(medias_anuais) if medias_anuais else None  # calcule a média do curso
        return round(media_do_curso, 1) if media_do_curso else None
    
    
    
    def __str__(self):
        return f'{self.aluno.nome} - {self.disciplina.nome} - {self.trimestre.nome} - {self.turma.nome}'

    