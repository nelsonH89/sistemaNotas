from django.db import models


# Create your models here.
class Aluno(models.Model):
    nome=models.CharField(max_length=80, verbose_name="Nome")
    data_de_nascimento=models.DateField(null=True, verbose_name="Data de nascimento")
    BI_No=models.CharField(max_length=14, null=True, unique=True, verbose_name="BI Nº")
    telefone=models.CharField(max_length=17, unique=True, blank=True, null=True, verbose_name="telefone")
    email=models.EmailField(max_length=40, blank=True, null=True, verbose_name="Email")
    responsavel=models.CharField(max_length=80, null=True, verbose_name="Responsável")
    telef_responsavel=models.CharField(max_length=17, null=True, verbose_name="Telefone do responsável")
    email_responsavel=models.EmailField(max_length=40, null=True, verbose_name="Email do responsável")

   
    def __str__(self):
        return self.nome
    
class AlunoImage(models.Model):
    image = models.FileField('Arquivos',upload_to='image', null=True, blank=True)
    aluno = models.ForeignKey(Aluno, related_name='alunos', on_delete=models.CASCADE, null=True, blank=True)
 
    def __str__(self):
        return self.product.name