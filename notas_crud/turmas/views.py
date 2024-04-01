from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView
from turmas.models import Turma
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.
@login_required
def index(request):
    # Busca todos os alunos
    turmas = Turma.objects.all()

    # Renderiza o template 'index.html' passando as disciplinas como contexto
    return render(request, 'turmas/index.html', {'turmas': turmas})


class TurmaList(LoginRequiredMixin, ListView):
    model = Turma
    queryset =Turma.objects.all()

class TurmaCreate(LoginRequiredMixin, CreateView):
    model = Turma
    fields = '__all__'
    success_url = reverse_lazy('turmas:index')

    def form_valid(self, form):
        nome = form.cleaned_data['nome']
        turno = form.cleaned_data['turno']
        if Turma.objects.filter(nome=nome, turno=turno).exists():
            # a turma já existe no banco de dados
            form.add_error('nome', 'Essa turma já existe')
            return self.form_invalid(form)
        return super().form_valid(form)
    
class TurmaUpdate(LoginRequiredMixin, UpdateView):
    model = Turma
    fields = '__all__'
    success_url = reverse_lazy('turmas:index')


class TurmaDetail(LoginRequiredMixin, DetailView):
    queryset = Turma.objects.all()
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['alunos'] = self.object.matricula_set.all()  # Recupera todos os alunos matriculados nesta turma
        return context

class TurmaDelete(LoginRequiredMixin, DeleteView):
    queryset = Turma.objects.all()
    success_url = reverse_lazy('turmas:index')
    
class TurmaDetailView(LoginRequiredMixin, DetailView):
    model = Turma
    template_name = 'turma.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['alunos'] = self.object.matricula_set.all()  # Recupera todos os alunos matriculados nesta turma
        return context