from django.urls import path 
from . import views 



urlpatterns = [
    path('liste_col/', views.afficher_colis, name="liste colis"),
    path('liste_col/rechercher_colis/', views.rechercher_colis, name="search colis"),
    path('liste_col/ajouter_colis/' , views.ajouter_colis , name="add colis" ),
    path('liste_col/<int:pk>/selected_row_info/', views.selected_row_info , name="colis row infos"),
    path('liste_col/<int:pk>/selected_row_info_to_print/', views.selected_row_info_to_print , name="colis row print"),
    path('liste_col/<int:pk>/selected_row_edit/', views.edit_colis , name="colis row edit"),
    path('liste_col/<int:pk>/selected_row_delete/', views.delete_colis , name="colis row deletion"),
]