from django.db import models

# Create your models here.
PERIODO_CHOICES = [
    ('Matutino', 'Matutino'),
    ('Vespertino', 'Vespertino'),
    ('Noturno', 'Noturno'),
]
class Periodo(models.Model):
    nome = models.CharField(max_length=15, choices=PERIODO_CHOICES)
    inicio = models.CharField(max_length=10)
    termina =models.CharField(max_length=10)

    def __str__(self):
        return self.nome
    