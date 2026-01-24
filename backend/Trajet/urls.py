from django.urls import path
from . import views

urlpatterns = [
    path('', views.trajet_data, name="trajets"),
    path('<int:trajet_id>/', views.trajet_id_view, name="trajets/id"),
    path('<int:trajet_id>/edit/', views.update_trajet, name="trajets/edit"),
    path('create/', views.create_trajet, name="trajets/create"),
    path('delete/', views.delete_trajets, name="trajets/delete"),
    path('info/', views.trajet_info, name="trajets/info"),
]
