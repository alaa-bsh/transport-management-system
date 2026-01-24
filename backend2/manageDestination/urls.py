from django.urls import path 
from . import views 

urlpatterns = [
    path('', views.destination_data, name="destinations"),
    path('<int:numBureau>/', views.destination_id_view, name="destinations/id"),
    path('<int:numBureau>/edit/', views.update_destination, name='destinations/edit'),
    path("create/", views.create_destination, name="destinations/create"),
    path("delete/", views.delete_destinations, name="destinations/delete"),
    path("info/", views.destination_info, name="destinations/info"),
]