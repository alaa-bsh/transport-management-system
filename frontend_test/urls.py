from django.urls import path
from . import views

urlpatterns = [ 
path('list_produits/', views.afficher_produits),
path("favoris/", views.favoris_view, name="favoris"),
path("clients/", views.client_view, name="client"),
path("clients/<int:client_id>", views.client_id_view, name="client/id"),
path("chauffeur/", views.chauffeur_view, name="chauffeur"),
path("vehicule/", views.vehicule_view, name="vehicule"),
path("destination/", views.destination_view, name="destination"),
path("type_service/", views.type_service_view, name="type_service"),
path("tarification/", views.tarification_view, name="tarification"),
path("expedition/", views.expedition_view, name="expedition"),
path("tournee/", views.tournee_view, name="tournee"),
path("facturation/", views.facturation_view, name="facturation"),
path("paiement/", views.facturation_view, name="paiement"),
path("incident/", views.incident_view, name="incident"),
path("reclamation/", views.reclamation_view, name="reclamation"),
path("dashboard/", views.dashboard_view, name="dashboard"),
path('clients/<int:client_id>/update/', views.update_client, name='update_client'),
path("clients/create/", views.create_client, name="create_client"),
]