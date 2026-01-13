
from django.http import JsonResponse
from django.shortcuts import redirect, render
from .forms import ColisForm
from .models import Colis
from django.core.paginator import Paginator


def colis_info(request):
    return JsonResponse({
        "poids": "number",
        "volume": "number",
        "description": "text",
    })


def afficher_colis(request):
    col = Colis.objects.all().order_by("id")
    paginator = Paginator(col, 12)
    page_nbr = request.GET.get("page")
    page_obj = paginator.get_page(page_nbr)

    return render(request,"pages/colis.html",{"page_obj": page_obj,"colis": page_obj,})


def rechercher_colis(request) :
    if request.method == "GET" :
        query= request.GET.get('searchFiled') # asm l field tae html

    if query :
        colis = Colis.objects.filter(id__contains = query)
        
        if colis :
            return render(request,"searchColis.html",{"colis":colis})
    return render(request,"pages/colis.html")



def ajouter_colis(request): #url done 
    if request.method == "POST":
        form = ColisForm(request.POST)

        if form.is_valid() :
            form.save()
            form = ColisForm()
            return render(request, "ajouterColis.html", {"form": form})
    else :
        form = ColisForm()
        return render (request , "ajouterColis.html" , {"form":form})
    



def edit_colis(request,pk): #url done 
    col = Colis.objects.get(id=pk)
    if request.method == 'POST':
            form = ColisForm(request.POST,instance=col)
            if form.is_valid() :
                form.save()
                return redirect("liste colis")
    
    else :
        form = ColisForm(instance=col)
        return render(request,"colisEdit.html",{"form":form})
    

def delete_colis(request,pk): #url done 
    col = Colis.objects.get(id=pk)
    if request.method== 'GET' :
        col.delete()
    return redirect("liste colis")



def selected_row_info(request,pk): #url done 
    col = Colis.objects.get(id=pk) # nheto fi col lista tae colis li their id = pk 
    return render (request,"infoColis.html", {"col":col}) # we send lel infColis html li reh tafficher l infos 


def selected_row_info_to_print(request,pk): #url done 
    col = Colis.objects.get(id=pk)
    return render (request,"infoColisPrint.html", {"col":col})