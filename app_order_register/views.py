from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import FormEntry
import json

@csrf_exempt  
def submit_form(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        entry = FormEntry.objects.create(
            client=data.get('client'),
            telefone=data.get('telefone'),
            carro=data.get('carro'),
            cor=data.get('cor'),
            placa=data.get('placa')

        )
        return JsonResponse({'status': 'success', 'id': entry.id})
    return JsonResponse({'error': 'Invalid request'}, status=400)