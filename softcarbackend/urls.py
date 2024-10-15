# softcarbackend/softcarbackend/urls.py

from django.contrib import admin
from django.urls import path
from app_user_register.views import submit_form
from django.http import JsonResponse


def health_check(request):
    return JsonResponse({"status": "ok"})

urlpatterns = [
    path('admin/', admin.site.urls),  
    path('submit/', submit_form, name='submit_form'),  
    path('order_register/', submit_form, name='submit_form_order'), 
    path('', health_check),  
]
