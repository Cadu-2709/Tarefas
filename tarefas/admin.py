from django.contrib import admin
from .models import Cliente, Tarefa

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'endereco')
    search_fields = ('nome',)

@admin.register(Tarefa)
class TarefaAdmin(admin.ModelAdmin):
    # Colunas que aparecerão na lista (igual à sua planilha)
    list_display = ('cliente', 'servico', 'empresa', 'status_colorido', 'prazo', 'get_tecnicos', 'updated_at')
    
    # Filtros laterais (excelente para achar rápido "O que a Proxmon tem pendente?")
    list_filter = ('status', 'empresa', 'tecnicos')
    
    # Barra de busca (busca por nome do cliente ou descrição do serviço)
    search_fields = ('cliente__nome', 'servico', 'descricao')
    
    # Facilita selecionar muitos técnicos sem segurar Ctrl
    filter_horizontal = ('tecnicos',)

    # Mostra os técnicos na lista (já que é ManyToMany)
    def get_tecnicos(self, obj):
        return ", ".join([t.username for t in obj.tecnicos.all()])
    get_tecnicos.short_description = 'Técnicos'

    # Um "mimo" visual: colorir o status na listagem
    def status_colorido(self, obj):
        from django.utils.html import format_html
        cores = {
            'nao_iniciado': 'red',
            'iniciado': 'orange',
            'feito': 'green',
        }
        return format_html(
            '<span style="color: {}; font-weight: bold;">{}</span>',
            cores.get(obj.status, 'black'),
            obj.get_status_display()
        )
    status_colorido.short_description = 'Status'