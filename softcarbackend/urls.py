from django.contrib import admin
from django.urls import path

from app_user_register.views import submit_form, getClientById, ClientListView

from django.http import JsonResponse


def health_check(request):
    return JsonResponse({"status": "ok"})


urlpatterns = [
    path('admin/', admin.site.urls),
    path('submit-form/', submit_form, name='submit-form'),
    path('', health_check, name='health_check'),
    path('clients/<int:id>/', getClientById, name='getClientById'),  
    path('clients/', ClientListView.as_view(), name='client-list'),
]
