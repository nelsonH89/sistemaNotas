from django.db import models

# Create your models here.
# App de Matriculas
class Matricula(models.Model):
    aluno = models.ForeignKey('alunos.Aluno', on_delete=models.CASCADE)
    turma = models.ForeignKey('turmas.Turma', on_delete=models.CASCADE)
    ano_letivo = models.ForeignKey('anos_letivos.AnoLetivo', on_delete=models.CASCADE)
    data_matricula = models.DateField(auto_now_add=True)

    class Meta:
        unique_together = ('aluno', 'turma', 'ano_letivo')

    def __str__(self):
        return str(f'{self.aluno.nome} - {self.turma.nome} - {self.ano_letivo.ano}')


