from django.urls import path
from . import views

urlpatterns = [
    path('', views.client_data, name="clients"),
    path('<int:client_id>/', views.client_id_view, name="clients/id"),
    path('<int:client_id>/edit/', views.update_client, name='clients/edit'),
    path("create/", views.create_client, name="clients/create"),
    path("delete/", views.delete_clients, name="clients/delete"),
    path("info/", views.client_info, name="clients/info"),
]
