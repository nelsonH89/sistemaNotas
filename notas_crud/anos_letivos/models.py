from django.db import models

# Create your models here.
class AnoLetivo(models.Model):
    nome=models.CharField(max_length=10)
    data_de_criacao = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.nome