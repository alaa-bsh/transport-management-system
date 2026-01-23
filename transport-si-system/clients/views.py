
from django.http import JsonResponse
from .models import Client

def client_list(request):
    clients = Client.objects.all()
    data = [
        {
            "id": c.id,
            "nom": c.nom,
            "prenom": c.prenom,
            "email": c.adrMAIL,
            "telephone": c.telephone,
            "solde": float(c.solde),
        }
        for c in clients
    ]
    return JsonResponse(data, safe=False)