
from django.urls import path 
from . import views 



urlpatterns = [
    path('liste_exp/', views.afficher_expedition, name="liste exp"),
    path('liste_exp/rechercher_exp/', views.rechercher_expedition, name="search exp "),
    path('liste_exp/ajouter_exp/' , views.ajouter_expedition , name="add exp" ),
    path('liste_exp/<int:pk>/selected_row_info/', views.selected_row_info , name="exp row infos"),
    path('liste_exp/<int:pk>/selected_row_info_to_print/', views.selected_row_info_to_print , name="exp row print"),
    path('liste_exp/<int:pk>/selected_row_edit/', views.edit_expedition , name="exp row edit"),
    path('liste_exp/<int:pk>/selected_row_delete/', views.delete_expedition , name="exp row deletion"),




    path('liste_tournee/', views.afficher_tournee, name="liste tournee"),
    path('liste_tournee/rechercher_tour/', views.rechercher_tournee, name="search tour "),
    path('liste_tournee/ajouter_tour/' , views.ajouter_tournee , name="add tour" ),
    path('liste_tournee/<int:pk>/selected_row_info/', views.selected_row_info , name="tour row infos"),
    path('liste_tournee/<int:pk>/selected_row_edit/', views.edit_tournee , name="tour row edit"),
    path('liste_tournee/<int:pk>/selected_row_delete/', views.delete_tournee , name="tour row deletion"),


    path('liste_fact/', views.afficher_facture, name="liste facture"),
    path('liste_fact/rechercher_fact/', views.rechercher_facture, name="search fact "),
    path('liste_fact/ajouter_fact/' , views.ajouter_facture , name="add fact" ),
    path('liste_fact/<int:pk>/selected_row_info/', views.selected_row_info , name="fact row infos"),
    path('liste_fact/<int:pk>/selected_row_info_to_print/', views.selected_row_info_to_print , name="fact row print"),
    path('liste_fact/<int:pk>/selected_row_edit/', views.edit_facture , name="fact row edit"),
    path('liste_fact/<int:pk>/selected_row_delete/', views.delete_facture , name="fact row deletion"),


]