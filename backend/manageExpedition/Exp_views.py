import json
from django.http import JsonResponse
from django.shortcuts import render
from .models import Expedition
from django.core.paginator import Paginator


def expedition_info(request):
    return JsonResponse({
        "id_client": "number",
        "statut": "string",
        "numBureau": "number",
        "id_tournée": "number",
        "service": "number",
    })


def expedition_data(request):

    table_fields = ["id_client" , "statut",  "numBureau", "id_tournée"]
    
    search_value = "" 
    exps = Expedition.objects.all().order_by("id") 

    if 'search' in request.GET:
        search_value = request.GET['search']
        if search_value:  
            exps = Expedition.objects.filter(id_client__nom__istartswith=search_value)

    sort_order = request.GET.get('sort', 'new')  

    if sort_order == 'old':
        exps = exps.order_by('id')  
    else:
        exps = exps.order_by('-id')  

    paginator = Paginator(exps, 12) 
    page_nbr = request.GET.get("page") 
    page_obj = paginator.get_page(page_nbr) 

    all_data = [
        {
            "id": e.id,
            "id_client": e.id_client.id,
            "statut": e.statut,
            "numBureau": e.numBureau.numBureau,
            "id_tournée": e.id_tournée.id if e.id_tournée else None,
         
        } for e in page_obj.object_list
    ]

    return render(request, 'pages/main.html', {
        "page_obj": page_obj,
        "expeditions": page_obj,
        "table_name": "Expeditions",
        "data_structure": all_data,
        "headers": table_fields,
        "sort_order": sort_order,
        "query": search_value
    })


def expedition_id_view(request, expedition_id):
    try:
        e = Expedition.objects.get(id=expedition_id)
        data = {
            "id": e.id,
            "id_client": e.id_client.id,
            "service": e.service.id if e.service else None,
            "statut": e.statut,
            "date_exped": e.date_exped.strftime("%Y-%m-%d %H:%M"),
            "numBureau": e.numBureau.numBureau,
            "id_tournée": e.id_tournée.id if e.id_tournée else None,
         
        }
        return JsonResponse(data)
    except Expedition.DoesNotExist:
        return JsonResponse({"error": "Expedition not found"}, status=404)
    
    
def update_expedition(request, expedition_id):
    if request.method == "POST":
        data = json.loads(request.body)

        try:
            e = Expedition.objects.get(id=expedition_id)
            from backend.clients.models import Client
            from backend.typeservice.models import TypeService
            from backend.manageDestination.models import Destination
            from backend.manageExpedition.models import Tournée

            if "id_client" in data:
                e.id_client = Client.objects.get(id=data["id_client"])
            if "service" in data:
                e.service = TypeService.objects.get(id=data["service"])
            if "statut" in data:
                e.statut = data["statut"]
            if "numBureau" in data:
                e.numBureau = Destination.objects.get(numBureau=data["numBureau"])
            if "id_tournée" in data:
                e.id_tournée = Tournée.objects.get(id=data["id_tournée"])

            e.save()
            
            return JsonResponse({
                "id": e.id,
                "id_client": e.id_client.id,
                "statut": e.statut,
                "numBureau": e.numBureau.numBureau,
                "id_tournée": e.id_tournée.id if e.id_tournée else None,
           
            })
        except Expedition.DoesNotExist:
            return JsonResponse({"error": "Expedition not found"}, status=404)
    return JsonResponse({"error": "Invalid request"}, status=400)


def create_expedition(request):
    if request.method == "POST":
        data = json.loads(request.body)

        from backend.clients.models import Client
        from backend.typeservice.models import TypeService
        from backend.manageDestination.models import Destination
        from backend.manageExpedition.models import Tournée

        e = Expedition.objects.create(
            id_client=Client.objects.get(id=data.get("id_client")),
            service=TypeService.objects.get(id=data.get("service")) if data.get("service") else None,
            statut=data.get("statut"),
            numBureau=Destination.objects.get(numBureau=data.get("numBureau")),
            id_tournée=Tournée.objects.get(id=data.get("id_tournée")) if data.get("id_tournée") else None,
        )

        return JsonResponse({
            "id": e.id,
            "id_client": e.id_client.id,
            "statut": e.statut,
            "numBureau": e.numBureau.numBureau,
            "id_tournée": e.id_tournée.id if e.id_tournée else None,
        
        })

    return JsonResponse({"error": "Invalid request"}, status=400)


def delete_expeditions(request):
    if request.method == "DELETE":
        data = json.loads(request.body)
        ids = data.get("ids", [])
        Expedition.objects.filter(id__in=ids).delete()
        return JsonResponse({"msg": "expeditions deleted"})
    return JsonResponse({"error": "Invalid request"}, status=400)
