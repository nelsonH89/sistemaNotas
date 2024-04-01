from django import forms
from alunos.models import Aluno, AlunoImage

class AlunoForm(forms.ModelForm):
    class Meta:
        model=Aluno
        fields = '__all__'
        data_de_nascimento = forms.DateField(
    label=(u'Data de Nascimento:'), 
    input_formats=["%d.%m.%Y",], 
    widget=forms.DateInput(format='%d.%m.%Y')
)

class AlunoImageForm(forms.ModelForm):
    class Meta:
        model = AlunoImage
        fields = ['image', 'aluno']