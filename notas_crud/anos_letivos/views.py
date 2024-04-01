from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView
from anos_letivos.models import AnoLetivo
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin



# Create your views here.
@login_required
def index(request):
    # Busca todos os alunos
    anos_letivos = AnoLetivo.objects.all()

    # Renderiza o template 'index.html' passando os alunos como contexto
    return render(request, 'anos_letivos/index.html', {'anos_letivos': anos_letivos})

@login_required
def pag_abertura(request):
    return render(request, 'index.html')

class AnoLetivoList(LoginRequiredMixin, ListView):
    model = AnoLetivo
    queryset =AnoLetivo.objects.all()

class AnoLetivoCreate(LoginRequiredMixin, CreateView):
    model = AnoLetivo
    fields = '__all__'
    success_url = reverse_lazy('anos_letivos:index')

    def form_valid(self, form):
        nome = form.cleaned_data['nome']
        if AnoLetivo.objects.filter(nome=nome).exists():
            # o ano letivo já existe no banco de dados
            form.add_error('nome', 'Esse ano letivo já existe')
            return self.form_invalid(form)
        return super().form_valid(form)
    
class AnoLetivoUpdate(LoginRequiredMixin, UpdateView):
    model = AnoLetivo
    fields = '__all__'
    success_url = reverse_lazy('anos_letivos:index')


class AnoLetivoDetail(LoginRequiredMixin, DetailView):
    queryset = AnoLetivo.objects.all()
    model = AnoLetivo
   
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['trimestres'] = self.object.trimestre_set.all()  # Recupera todos os trimestres associados a este ano letivo
        return context
    
    
class AnoLetivoDetailView(LoginRequiredMixin, DetailView):
    model = AnoLetivo
    template_name = 'anos_letivos.anoletivo.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['trimestres'] = self.object.trimestre_set.all()  # Recupera todos os trimestres associados a este ano letivo
        return context

class AnoLetivoDelete(LoginRequiredMixin, DeleteView):
    queryset = AnoLetivo.objects.all()
    success_url = reverse_lazy('anos_letivos:index')