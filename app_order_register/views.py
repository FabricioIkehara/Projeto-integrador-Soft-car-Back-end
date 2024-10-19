from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import FormEntry
import json

@csrf_exempt
def submit_form(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            entry = FormEntry.objects.create(
                client=data.get('client'),
                telefone=data.get('telefone'),
                carro=data.get('carro'),
                cor=data.get('cor'),
                placa=data.get('placa'),
                observacao=data.get('observacao')
            )
            return JsonResponse({'status': 'success', 'id': entry.id})
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON format'}, status=400)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
    return JsonResponse({'error': 'Invalid request'}, status=400)

@csrf_exempt
def submit_order(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            # Lógica para registrar um pedido
            # Por exemplo, pode-se criar um novo modelo para pedidos
            return JsonResponse({'status': 'success'})
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON format'}, status=400)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
    return JsonResponse({'error': 'Invalid request'}, status=400)
