from django.urls import path 
from . import views 



urlpatterns = [
    path('', views.afficher_colis, name="liste colis"),
    path("colis/info/", views.colis_info, name="colis_info"),
    path('rechercher_colis/', views.rechercher_colis, name="search colis"),
    path('ajouter_colis/' , views.ajouter_colis , name="add colis" ),
    path('<int:pk>/selected_row_info/', views.selected_row_info , name="colis row infos"),
    path('<int:pk>/selected_row_info_to_print/', views.selected_row_info_to_print , name="colis row print"),
    path('<int:pk>/selected_row_edit/', views.edit_colis , name="colis row edit"),
    path('<int:pk>/selected_row_delete/', views.delete_colis , name="colis row deletion"),
]