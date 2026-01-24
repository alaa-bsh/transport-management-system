from django.urls import path
from . import Chauffeur_views , Vehicule_views

urlpatterns = [
    path('', Vehicule_views.vehicule_data, name="vehicules"),
    path('<int:vehicule_id>/', Vehicule_views.vehicule_id_view, name="vehicules/id"),
    path('<int:vehicule_id>/edit/', Vehicule_views.update_vehicule, name='vehicules/edit'),
    path("create/", Vehicule_views.create_vehicule, name="vehicules/create"),
    path("delete/", Vehicule_views.delete_vehicule, name="vehicules/delete"),
    path("info/", Vehicule_views.vehicule_info, name="vehicules/info"),
]
