from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from disciplinas.models import Disciplina

# Create your views here.
@login_required
def index(request):
    # Busca todos os alunos
    disciplinas = Disciplina.objects.all()

    # Renderiza o template 'index.html' passando as disciplinas como contexto
    return render(request, 'disciplinas/index.html', {'disciplinas': disciplinas})

class DisciplinaList(LoginRequiredMixin, ListView):
    model = Disciplina
    queryset =Disciplina.objects.all()

class DisciplinaCreate(LoginRequiredMixin, CreateView):
    model = Disciplina
    fields = '__all__'
    success_url = reverse_lazy('disciplinas:index')

    def form_valid(self, form):
        nome = form.cleaned_data['nome']
        if Disciplina.objects.filter(nome=nome).exists():
            # a disciplina já existe no banco de dados
            form.add_error('nome', 'Essa disciplina já existe')
            return self.form_invalid(form)
        return super().form_valid(form)
    
class DisciplinaUpdate(LoginRequiredMixin, UpdateView):
    model = Disciplina
    fields = '__all__'
    success_url = reverse_lazy('disciplinas:index')


class DisciplinaDetail(LoginRequiredMixin, DetailView):
    queryset = Disciplina.objects.all()

class DisciplinaDelete(LoginRequiredMixin, DeleteView):
    queryset = Disciplina.objects.all()
    success_url = reverse_lazy('disciplinas:index')