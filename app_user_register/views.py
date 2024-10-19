from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import FormEntry

@csrf_exempt
def submit_form(request):
    print("Request body:", request.body) 
    if request.method == 'POST':
        try:
            if not request.body:
                return JsonResponse({'error': 'Empty body'}, status=400)

            data = json.loads(request.body)

            required_fields = ['client', 'telefone', 'carro', 'cor', 'placa', 'observacao']
            for field in required_fields:
                if field not in data:
                    return JsonResponse({'error': f'Missing field: {field}'}, status=400)

            entry = FormEntry.objects.create(
                client=data['client'],
                telefone=data['telefone'],
                carro=data['carro'],
                cor=data['cor'],
                placa=data['placa'],
                observacao=data['observacao']
            )
            return JsonResponse({'status': 'success', 'id': entry.id})
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON format'}, status=400)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)

    return JsonResponse({'error': 'Invalid request method'}, status=400)
