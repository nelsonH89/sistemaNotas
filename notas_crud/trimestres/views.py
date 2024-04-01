from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from trimestres.models import Trimestre

# Create your views here.
@login_required
def index(request):
    # Busca todos os alunos
    trimestres = Trimestre.objects.all()

    # Renderiza o template 'index.html' passando as disciplinas como contexto
    return render(request, 'trimestres/index.html', {'trimestres': trimestres})

class TrimestreList(LoginRequiredMixin, ListView):
    model = Trimestre
    queryset =Trimestre.objects.all()

class TrimestreCreate(LoginRequiredMixin, CreateView):
    model = Trimestre
    fields = '__all__'
    success_url = reverse_lazy('trimestres:list')

    def form_valid(self, form):
        trimestre = form.cleaned_data['trimestre']
        ano_letivo = form.cleaned_data['ano_letivo']
        if Trimestre.objects.filter(trimestre=trimestre, ano_letivo=ano_letivo).exists():
            # este trimestre já existe no banco de dados
            form.add_error('trimestre', 'Esse trimestre já existe')
            return self.form_invalid(form)
        # Cadastre o novo trimestre
        return super().form_valid(form)
    
class TrimestreUpdate(LoginRequiredMixin, UpdateView):
    model = Trimestre
    fields = '__all__'
    success_url = reverse_lazy('trimestres:list')


class TrimestreDetail(LoginRequiredMixin, DetailView):
    queryset = Trimestre.objects.all()

class TrimestreDelete(LoginRequiredMixin, DeleteView):
    queryset = Trimestre.objects.all()
    success_url = reverse_lazy('trimestres:list')