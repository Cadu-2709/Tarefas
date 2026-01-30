from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_tarefas, name='lista_tarefas'),
    path('nova/', views.nova_tarefa, name='nova_tarefa'),           # <--- Nova
    path('editar/<int:id>/', views.editar_tarefa, name='editar_tarefa'),
     path('excluir/<int:id>/', views.excluir_tarefa, name='excluir_tarefa'), # <--- Nova
]