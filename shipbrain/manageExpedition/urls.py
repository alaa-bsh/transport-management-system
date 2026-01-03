
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
]