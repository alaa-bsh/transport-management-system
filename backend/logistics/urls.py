from django.urls import path
from . import Chauffeur_views 

urlpatterns = [
    path('', Chauffeur_views.chauffeur_data, name="chauffeurs"),
    path('<int:chauffeur_id>/', Chauffeur_views.chauffeur_id_view, name="chauffeurs/id"),
    path('<int:chauffeur_id>/edit/', Chauffeur_views.update_chaffeur, name='chauffeurs/edit'),
    path("create/", Chauffeur_views.create_chaffeur, name="chauffeurs/create"),
    path("delete/", Chauffeur_views.delete_chauffeur, name="chauffeurs/delete"),
    path("info/", Chauffeur_views.chauffeur_info, name="chauffeurs/info"),
]
