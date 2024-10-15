# softcarbackend/softcarbackend/urls.py

from django.contrib import admin
from django.urls import path
from app_user_register.views import submit_form
from django.http import JsonResponse

# Função para retornar um status de verificação
def health_check(request):
    return JsonResponse({"status": "ok"})

urlpatterns = [
    path('admin/', admin.site.urls),  # Rota para o painel administrativo do Django
    path('submit/', submit_form, name='submit_form'),  # Rota para o formulário de submissão
    path('order_register/', submit_form, name='submit_form_order'),  # Rota para registro de pedidos
    path('', health_check),  # Rota para verificação do servidor (opcional)
]
