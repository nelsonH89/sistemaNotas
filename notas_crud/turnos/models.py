from django.db import models

# Create your models here.
TURNOS_CHOICES=[
    ('MATUTINO', 'Matutino'),
    ('VESPERTINO', 'Vespertino'),
    ('NOTURNO', 'Noturno'),
]
class Turno(models.Model):

    nome=models.CharField(max_length=30, null=True, choices=TURNOS_CHOICES)
    entrada=models.CharField(max_length=15, blank=True, null=True)
    saida=models.CharField(max_length=15, null=True)

    def __str__(self):
        return self.nome
    