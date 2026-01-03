from django.shortcuts import redirect, render
from .forms import ExpeditionForm
from .models import Expedition
from django.core.paginator import Paginator


def afficher_expedition(request): #url done 
    exp = Expedition.objects.all().order_by("id")
    paginator = Paginator(exp, 12)  
    page_nbr = request.GET.get("page")
    page = paginator.get_page(page_nbr)
    return render(request,"journalExp.html",{"page": page})




def rechercher_expedition(request) :
    if request.method == "GET" :
        query= request.GET.get('searchFiled') # asm l field tae html

    if query :
        expeditions = Expedition.objects.filter(id__contains = query)
        
        if expeditions :
            return render(request,"searchExp.html",{"expeditions":expeditions})
    return render(request,"journalExp.html")



def ajouter_expedition(request): #url done 
    if request.method == "POST":
        form = ExpeditionForm(request.POST)

        if form.is_valid() :
            form.save()
            form = ExpeditionForm()
            return render(request, "ajouterExp.html", {"form": form})
    else :
        form = ExpeditionForm()
        return render (request , "ajouterExp.html" , {"form":form})
    



def edit_expedition(request,pk): #url done 
    exp = Expedition.objects.get(id=pk)
    if request.method == 'POST':
            form = ExpeditionForm(request.POST,instance=exp)
            if form.is_valid() :
                form.save()
                return redirect("liste exp")
    
    else :
        form = ExpeditionForm(instance=exp)
        return render(request,"expEdit.html",{"form":form})
    

def delete_expedition(request,pk): #url done 
    exp =Expedition.objects.get(id=pk)
    if request.method== 'GET' :
        exp.delete()
    return redirect("liste exp")



def selected_row_info(request,pk): #url done 
    exp = Expedition.objects.get(id=pk)
    return render (request,"infoExp.html", {"exp":exp})


def selected_row_info_to_print(request,pk): #url done 
    exp = Expedition.objects.get(id=pk)
    return render (request,"infoExpPrint.html", {"exp":exp})