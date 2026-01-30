from django.contrib import admin
from django.urls import path, include # <--- Adicione o include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('tarefas.urls')), # <--- Isso faz a home do site carregar suas tarefas
]