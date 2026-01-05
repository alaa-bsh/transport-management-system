from django.urls import path 
from . import views 



urlpatterns = [
    path('liste_dest/', views.afficher_destination, name="liste destination"),
    path('liste_dest/rechercher_dest/', views.rechercher_destination, name="search dest "),
    path('liste_dest/ajouter_dest/' , views.ajouter_destination , name="add dest" ),
    path('liste_dest/<int:pk>/selected_row_edit/', views.edit_destination , name="dest row edit"),
    path('liste_dest/<int:pk>/selected_row_delete/', views.delete_destination , name="dest row deletion"),
]