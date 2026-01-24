from django.urls import path
from . import views

urlpatterns = [
    path('', views.reclamation_data, name="reclamations"),
    path('<int:reclamation_id>/', views.reclamation_id_view, name="reclamations/id"),
    path('<int:reclamation_id>/edit/', views.update_reclamation, name='reclamations/edit'),
    path("create/", views.create_reclamation, name="reclamations/create"),
    path("delete/", views.delete_reclamations, name="reclamations/delete"),
    path("info/", views.reclamation_info, name="reclamations/info"),
]