from django.db import models
from anos_letivos.models import AnoLetivo

# Create your models here.

TRIMESTRES_CHOICE = [
    '1ºTrimestre',
    '2ºTrimestre',
    '3ºTrimestre',
    'Exame',
    'Recurso'
]

class Trimestre(models.Model):
   
    trimestre = models.CharField(max_length=15, choices=[(choice, choice) for choice in TRIMESTRES_CHOICE], null=True)
    ano_letivo = models.ForeignKey('anos_letivos.AnoLetivo', on_delete=models.CASCADE, null=True)
       
    def __str__(self):
       
        return self.trimestre

