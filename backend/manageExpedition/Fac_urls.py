from django.urls import path
from . import fac_views as views

urlpatterns = [
    path('', views.facture_data, name="factures"),
    path('<int:facture_id>/', views.facture_id_view, name="factures/id"),
    path('<int:facture_id>/edit/', views.update_facture, name='factures/edit'),
    path("create/", views.create_facture, name="factures/create"),
    path("delete/", views.delete_factures, name="factures/delete"),
    path("info/", views.facture_info, name="factures/info"),
]
