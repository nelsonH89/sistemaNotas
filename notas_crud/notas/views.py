from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView
from notas.models import Nota
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
@login_required
def index(request):
    # Busca todos os alunos
    notas = Nota.objects.all()

    # Renderiza o template 'index.html' passando as disciplinas como contexto
    return render(request, 'notas/index.html', {'notas': notas})
@login_required
def pag_abertura(request):
    return render(request, 'index2.html')

class NotaList(LoginRequiredMixin, ListView):
    model = Nota
    queryset =Nota.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        for nota in context['object_list']:
            nota.media = nota.media()
        return context

class NotaCreate(LoginRequiredMixin, CreateView):
    model = Nota
    fields = '__all__'
    success_url = reverse_lazy('notas:index')

   

    
class NotaUpdate(LoginRequiredMixin, UpdateView):
    model = Nota
    fields = '__all__'
    success_url = reverse_lazy('notas:index')


class NotaDetail(LoginRequiredMixin, DetailView):
    queryset = Nota.objects.all()

class NotaDelete(LoginRequiredMixin, DeleteView):
    queryset = Nota.objects.all()
    success_url = reverse_lazy('notas:index')