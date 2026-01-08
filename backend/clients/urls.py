from django.urls import path
from . import views

urlpatterns = [
    path('', views.client_view, name="clients"),
    path('<int:client_id>', views.client_id_view, name="client/id"),
    path('<int:client_id>/update/', views.update_client, name='update_client'),
    path("create/", views.create_client, name="create_client"),
]
