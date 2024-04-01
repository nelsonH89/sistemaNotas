from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from matriculas.models import Matricula

# Create your views here.
@login_required
def index(request):
    # Busca todos os alunos
    matriculas = Matricula.objects.all()

    # Renderiza o template 'index.html' passando as disciplinas como contexto
    return render(request, 'matriculas/index.html', {'matriculas': matriculas})

class MatriculaList(LoginRequiredMixin, ListView):
    model = Matricula
    queryset =Matricula.objects.all()

class MatriculaCreate(LoginRequiredMixin, CreateView):
    model = Matricula
    fields = '__all__'
    success_url = reverse_lazy('matriculas:index')


class MatriculaUpdate(LoginRequiredMixin, UpdateView):
    model = Matricula
    fields = '__all__'
    success_url = reverse_lazy('matriculas:index')


class MatriculaDetail(LoginRequiredMixin, DetailView):
    queryset = Matricula.objects.all()

class MatriculaDelete(LoginRequiredMixin, DeleteView):
    queryset = Matricula.objects.all()
    success_url = reverse_lazy('matriculas:index')