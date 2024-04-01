from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView
from periodos.models import Periodo

# Create your views here.
class PeriodoList(ListView):
    model = Periodo
    queryset =Periodo.objects.all()

class PeriodoCreate(CreateView):
    model = Periodo
    fields = '__all__'
    success_url = reverse_lazy('periodos:list')

    def form_valid(self, form):
        nome = form.cleaned_data['nome']
        if Periodo.objects.filter(nome=nome).exists():
            # este periodo já existe no banco de dados
            form.add_error('nome', 'Esse periodo já existe')
            return self.form_invalid(form)
        return super().form_valid(form)
    
class PeriodoUpdate(UpdateView):
    model = Periodo
    fields = '__all__'
    success_url = reverse_lazy('periodos:list')


class PeriodoDetail(DetailView):
    queryset = Periodo.objects.all()

class PeriodoDelete(DeleteView):
    queryset = Periodo.objects.all()
    success_url = reverse_lazy('periodos:list')