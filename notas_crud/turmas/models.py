from django.db import models

# Create your models here.
class Turma(models.Model):
    nome=models.CharField(max_length=4, unique=True)
    turno=models.ForeignKey('turnos.Turno', on_delete=models.CASCADE, null=True)
    anoLetivo=models.ForeignKey('anos_letivos.AnoLetivo', on_delete=models.CASCADE)

    def __str__(self):
        return self.nome