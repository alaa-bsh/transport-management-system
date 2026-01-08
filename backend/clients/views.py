import json
from django.http import JsonResponse
from django.shortcuts import render
from .models import Client

def client_view(request):
    clients = Client.objects.all()
    data = [
        {
            "id": c.id,
            "nom": c.nom,
            "prenom": c.prenom,
            "email": c.email,
            "telephone": c.telephone,
            "solde": float(c.solde),
            "date_creation": c.date_creation.strftime("%Y-%m-%d %H:%M"),
        }
        for c in clients
    ]
    return render(request, 'pages/tables/client.html', {"clients": clients})

def client_id_view(request, client_id):
    try:
        client = Client.objects.get(id=client_id)
        data = {
            "id": client.id,
            "nom": client.nom,
            "prenom": client.prenom,
            "telephone": client.telephone,
            "email": client.email,
            "solde": str(client.solde),
            "date_creation": client.date_creation.strftime("%Y-%m-%d %H:%M"),
        }
        return JsonResponse(data)
    except Client.DoesNotExist:
        return JsonResponse({"error": "Client not found"}, status=404)
    
def update_client(request, client_id):
    if request.method == "POST":
        data = json.loads(request.body)

        try:
            client = Client.objects.get(id=client_id)
            client.nom = data.get("nom", client.nom)
            client.prenom = data.get("prenom", client.prenom)
            client.telephone = data.get("telephone", client.telephone)
            client.email = data.get("email", client.email)
            client.solde = data.get("solde", client.solde)
            client.save()
            
            return JsonResponse({
                "id": client.id,
                "nom": client.nom,
                "prenom": client.prenom,
                "telephone": client.telephone,
                "email": client.email,
                "solde": client.solde
            })
        except Client.DoesNotExist:
            return JsonResponse({"error": "Client not found"}, status=404)
    return JsonResponse({"error": "Invalid request"}, status=400)

def create_client(request):
    if request.method == "POST":
        data = json.loads(request.body)

        client = Client.objects.create(
            nom=data.get("nom"),
            prenom=data.get("prenom"),
            telephone=data.get("telephone"),
            email=data.get("email"),
            solde=data.get("solde", 0)
        )

        return JsonResponse({
            "id": client.id,
            "nom": client.nom,
            "prenom": client.prenom,
            "telephone": client.telephone,
            "email": client.email,
            "solde": client.solde,
            "date_creation": client.date_creation.strftime("%Y-%m-%d %H:%M")
        })

    return JsonResponse({"error": "Invalid request"}, status=400)