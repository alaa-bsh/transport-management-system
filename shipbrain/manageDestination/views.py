
from django.shortcuts import redirect, render
from .forms import DestinationForm
from .models import Destination
from django.core.paginator import Paginator


def afficher_destination(request): #url done 
    dest = Destination.objects.all().order_by("id")
    paginator = Paginator(dest, 12)  
    page_nbr = request.GET.get("page")
    page = paginator.get_page(page_nbr)
    return render(request,"journalDest.html",{"page": page})




def rechercher_destination(request) :
    if request.method == "GET" :
        query= request.GET.get('searchFiled') # asm l field tae html

    if query :
        dest = Destination.objects.filter(numBureau__contains = query) # putting les dest li are accurate f dest
        
        if dest :
            return render(request,"searchDest.html",{"dest":dest})
    return render(request,"journalDest.html")



def ajouter_destination(request): #url done 
    if request.method == "POST":
        form = DestinationForm(request.POST)

        if form.is_valid() :
            form.save()
            form = DestinationForm()
            return render(request, "ajouterDest.html", {"form": form})
    else :
        form = DestinationForm()
        return render (request , "ajouterDest.html" , {"form":form})
    



def edit_destination(request,pk): #url done 
    dest = Destination.objects.get(id=pk)
    if request.method == 'POST':
            form = DestinationForm(request.POST,instance=dest)
            if form.is_valid() :
                form.save()
                return redirect("liste destination")
    
    else :
        form = DestinationForm(instance=dest)
        return render(request,"destEdit.html",{"form":form})
    

def delete_destination(request,pk): #url done 
    dest = Destination.objects.get(id=pk)
    if request.method== 'GET' :
        dest.delete()
    return redirect("liste destination")

