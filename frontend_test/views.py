import json
from django.http import JsonResponse
from django.shortcuts import render
from .models import Product , Client

def afficher_produits(request):
    produits = Product.objects.all() 
    return render(request, 'pages/test.html', {"products": produits})

def favoris_view(request):
    produits = Product.objects.all()
    return render(request, 'pages/favoris.html', {"products": produits})

def client_view(request):
    clients = Client.objects.all()
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


def chauffeur_view(request):
    produits = Product.objects.all()
    return render(request, 'pages/tables/chauffeur.html', {"products": produits})

def vehicule_view(request):
    produits = Product.objects.all()
    return render(request, 'pages/tables/vehicule.html', {"products": produits})

def destination_view(request):
    produits = Product.objects.all()
    return render(request, 'pages/tables/destination.html', {"products": produits})

def type_service_view(request):
    produits = Product.objects.all()
    return render(request, 'pages/tables/type_service.html', {"products": produits})

def tarification_view(request):
    produits = Product.objects.all()
    return render(request, 'pages/tables/tarification.html', {"products": produits})

def expedition_view(request):
    produits = Product.objects.all()
    return render(request, 'pages/expedition.html', {"products": produits})

def tournee_view(request):
    produits = Product.objects.all()
    return render(request, 'pages/expedition.html', {"products": produits , "page_name": "Tournee"})

def facturation_view(request):
    produits = Product.objects.all()
    return render(request, 'pages/facturation.html', {"products": produits})

def paiement_view(request):
    produits = Product.objects.all()
    return render(request, 'pages/paiement.html', {"products": produits})

def incident_view(request):
    produits = Product.objects.all()
    return render(request, 'pages/incident.html', {"products": produits})

def reclamation_view(request):
    produits = Product.objects.all()
    return render(request, 'pages/reclamation.html', {"products": produits})

def dashboard_view(request):
    produits = Product.objects.all()
    return render(request, 'pages/dashboard.html', {"products": produits})
