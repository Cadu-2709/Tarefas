from django.db import models
from django.contrib.auth.models import User

class Cliente(models.Model):
    nome = models.CharField(max_length=200)
    endereco = models.CharField(max_length=255, blank=True, null=True)
    
    def __str__(self):
        return self.nome

class Tarefa(models.Model):
    STATUS_CHOICES = [
        ('nao_iniciado', 'Não Iniciado'),
        ('iniciado', 'Iniciado'),
        ('feito', 'Feito'),
    ]
    
    EMPRESA_CHOICES = [
        ('proxmon', 'Proxmon'),
        ('eletros', 'Eletros'),
        # Adicione outras empresas do grupo aqui
    ]

    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    servico = models.CharField(max_length=255, verbose_name="Serviço/Título")
    descricao = models.TextField(blank=True, verbose_name="Detalhes do Serviço")
    
    # Empresa do grupo (Proxmon/Eletros)
    empresa = models.CharField(max_length=50, choices=EMPRESA_CHOICES, default='proxmon')
    
    # Técnicos: ManyToMany permite selecionar "Cadu" e "Fernando" para a mesma tarefa
    tecnicos = models.ManyToManyField(User, related_name='tarefas', blank=True)
    
    # O campo "Atualização" da planilha parece um log de status. 
    ultima_atualizacao = models.TextField(blank=True, verbose_name="Status/Obs Atual")
    
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='nao_iniciado')
    prazo = models.DateField(null=True, blank=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.cliente} - {self.servico}"