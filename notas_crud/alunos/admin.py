from django.contrib import admin
from django.http import HttpResponse
from alunos.models import Aluno

from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter, A4, landscape
from reportlab.platypus import Table, TableStyle
from reportlab.lib import colors

@admin.register(Aluno) 
class AlunoAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'nome',
        'data_de_nascimento',
        'BI_No',
        'telefone',
        'email',
        'responsavel',
        'telef_responsavel',
        'email_responsavel'
    )
    
    def download_pdf(self, request, queryset):
        model_name = self.model.__name__
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = f'attachment; filename={model_name}.pdf'
        
        pdf = canvas.Canvas(response, pagesize=landscape(letter))  # Altere para landscape(letter)
        pdf.setTitle('PDF Report')
        
        ordered_queryset = queryset.order_by('id')
        
        headers = [field.verbose_name for field in self.model._meta.fields]
        data = [headers]
        
        for obj in ordered_queryset:
            data_row = [str(getattr(obj, field.name)) for field in self.model._meta.fields]
            data.append(data_row)
            
        table = Table(data, colWidths=72, rowHeights=30)
        table.setStyle(TableStyle(
            [
              ('BACKGROUND', (0,0), (-1,0), colors.grey),
              ('GRID', (0,0), (-1,-1), 1, colors.black),
              ('LEFTPADDING', (0,0), (-1,-1), 3),
              ('RIGHTPADDING', (0,0), (-1,-1), 3),
              ('TOPPADDING', (0,0), (-1,-1), 3),
              ('BOTTOMPADDING', (0,0), (-1,-1), 3),
            ]
        ))
        
        canvas_width = 600
        canvas_height = 600
        
        table.wrapOn(pdf, canvas_width, canvas_height)
        table.drawOn(pdf, 40, canvas_height - len(data))
        
        pdf.save()
        return response
    
    download_pdf.short_description = "Download seleted items as PDF"
    actions = [download_pdf]
