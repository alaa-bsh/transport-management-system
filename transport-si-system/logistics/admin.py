from django.contrib import admin
from .models import Chauffeur, Vehicule

@admin.register(Chauffeur)
class ChauffeurAdmin(admin.ModelAdmin):
    list_display = ('nom', 'prenom', 'numPermis', 'Disponibilite')
    list_filter = ('Disponibilite',)

@admin.register(Vehicule)
class VehiculeAdmin(admin.ModelAdmin):
    list_display = ('numImmat', 'type_vehicule', 'etat', 'capacitePoids')
    list_filter = ('etat', 'type_vehicule')