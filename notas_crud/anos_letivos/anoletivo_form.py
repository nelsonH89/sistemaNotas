from django import forms
from anos_letivos.models import AnoLetivo

class AnoLetivoForm(forms.ModelForm):
    class Meta:
        model=AnoLetivo
        fields = '__all__'
        inicio = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
        fim = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))