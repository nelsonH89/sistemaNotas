from django import forms
from professores.models import Professor

class ProfessorForms(forms.ModelForm):
    class Meta:
        model=Professor
        fields = '__all__'
        data_de_nasc = forms.DateField(
    label=(u'Data de Nascimento:'), 
    input_formats=["%d.%m.%Y",], 
    widget=forms.DateInput(format='%d.%m.%Y')
)
