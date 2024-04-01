from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView
from turnos.models import Turno
from turmas.models import Turma
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
@login_required
def index(request):
    # Busca todos os alunos
    turnos = Turno.objects.all()

    # Renderiza o template 'index.html' passando as disciplinas como contexto
    return render(request, 'turnos/index.html', {'turnos': turnos})

class TurnoList(LoginRequiredMixin, ListView):
    model = Turno
    queryset =Turno.objects.all()

class TurnoCreate(LoginRequiredMixin, CreateView):
    model = Turno
    fields = '__all__'
    success_url = reverse_lazy('turnos:list')

    def form_valid(self, form):
        nome = form.cleaned_data['nome']
        if Turno.objects.filter(nome=nome).exists():
            # a turno já existe no banco de dados
            form.add_error('nome', 'Esse turno já existe')
            return self.form_invalid(form)
        return super().form_valid(form)
    
class TurnoUpdate(LoginRequiredMixin, UpdateView):
    model = Turno
    fields = '__all__'
    success_url = reverse_lazy('turnos:list')


class TurnoDetail(LoginRequiredMixin, DetailView):
    queryset = Turno.objects.all()

class TurnoDelete(LoginRequiredMixin, DeleteView):
    queryset = Turno.objects.all()
    success_url = reverse_lazy('turnos:list')