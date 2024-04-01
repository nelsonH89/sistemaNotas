from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView

from professores.models import Professor
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
@login_required
def index(request):
    # Busca todos os alunos
    professores = Professor.objects.all()

    # Renderiza o template 'index.html' passando as disciplinas como contexto
    return render(request, 'professores/index.html', {'professores': professores})


class ProfessorList(LoginRequiredMixin, ListView):
    model = Professor
    queryset = Professor.objects.all()

class ProfessorCreate(LoginRequiredMixin, CreateView):
    model = Professor
    fields = '__all__'
    success_url = reverse_lazy('professores:index')

    def form_valid(self, form):
        nome = form.cleaned_data['nome']
        if Professor.objects.filter(nome=nome).exists():
            # O professor já existe no banco de dados
            form.add_error('nome', 'Professor já existente')
            return self.form_invalid(form)
        return super().form_valid(form)
    
class ProfessorUpdate(LoginRequiredMixin, UpdateView):
    model = Professor
    fields = '__all__'
    success_url = reverse_lazy('professores:index')


class ProfessorDetail(LoginRequiredMixin, DetailView):
    queryset = Professor.objects.all()

class ProfessorDelete(LoginRequiredMixin, DeleteView):
    queryset = Professor.objects.all()
    success_url = reverse_lazy('professores:index')

class ProfessorView(LoginRequiredMixin, DetailView):
    def get(self, request, professor_id):
        professor = Professor.objects.get(id=professor_id)
        disciplinas = professor.disciplina_set.all()
        return render(request, 'professor.html', {'professor': professor, 'disciplinas': disciplinas})