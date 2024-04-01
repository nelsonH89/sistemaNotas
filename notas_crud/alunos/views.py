import csv
import datetime
import tempfile
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from alunos.models import Aluno
from django.template.loader import render_to_string

from alunos import alunoForms  
from .models import Aluno, AlunoImage
from django.http import HttpResponse
from alunos.models import Aluno
from django.contrib.auth.mixins import LoginRequiredMixin
from django.template.loader import get_template
from django.http import HttpResponseServerError
from django.template.loader import get_template
from django.core.files.base import ContentFile
import pdfkit
from django.contrib.auth.mixins import LoginRequiredMixin
    
# Create your views here.
@login_required
def index(request):
    # Busca todos os alunos
    alunos = Aluno.objects.all()

    # Renderiza o template 'index.html' passando os alunos como contexto
    return render(request, 'alunos/index.html', {'alunos': alunos})

@login_required
def pag_abertura(request):
    return render(request, 'index.html')


class AlunoList(LoginRequiredMixin, ListView):
    model = Aluno
    queryset = Aluno.objects.all()

class AlunoCreate(LoginRequiredMixin, CreateView):
    model = Aluno
    fields = '__all__'
    success_url = reverse_lazy('alunos:list')

    def form_valid(self, form):
        nome = form.cleaned_data['nome']
        if Aluno.objects.filter(nome=nome).exists():
            # O aluno já existe no banco de dados
            form.add_error('nome', 'Aluno já existente')
            return self.form_invalid(form)
        return super().form_valid(form)
    
#def form_aluno(request):
   # form = alunoForms.AlunoForm()
    
    #if request.method == 'POST':
     #   form = alunoForms(request.POST, request.FILES)
      #  if form.is_valid():
     #       aluno = form.save()
            
       #     files = request.FILES.getlist('alunos')
      #      if files:
      #          for f in files:
      #              AlunoImage.objects.create(
      #                  aluno=aluno, 
      #                  image=f)
       #     return redirect('index')     
       # return render(request, 'aluno_form.html', {'form': form}) 

class AlunoUpdate(LoginRequiredMixin, UpdateView):
    model = Aluno
    fields = '__all__'
    #template_name = "aluno_alterar.html"
    success_url = reverse_lazy('alunos:list')

class AlunoDetail(LoginRequiredMixin, DetailView):
    queryset = Aluno.objects.all()

class AlunoDelete(LoginRequiredMixin, DeleteView):
    queryset = Aluno.objects.all()
    success_url = reverse_lazy('alunos:list')
    
    #Código para gerar um arquivo em PDF

def render_to_pdf(template_src, context_dict={}):
    template = get_template(template_src)
    html = template.render(context_dict)

    options = {
        'page-size': 'A4',
        'encoding': "UTF-8",
        'no-outline': None,
    }

    pdf = pdfkit.from_string(html, False, options=options)

    if pdf:
        return ContentFile(pdf)
    else:
        return HttpResponseServerError("Erro ao gerar o PDF.")

@login_required
def alunos_index(request):
    alunos = Aluno.objects.all()
    data = {'alunos': alunos}
    pdf = render_to_pdf('alunos/index.html', data)
    
    if pdf:
        response = HttpResponse(pdf, content_type='application/pdf')
        response['Content-Disposition'] = 'inline; filename="alunos.pdf"'
        return response
    else:
        return HttpResponseServerError("Erro ao gerar o PDF.")
    


 
