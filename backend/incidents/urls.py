from django.urls import path
from . import views

urlpatterns = [
    path('', views.incident_data, name="incidents"),
    path('<int:incident_id>/', views.incident_id_view, name="incidents/id"),
    path('<int:incident_id>/edit/', views.update_incident, name='incidents/edit'),
    path("create/", views.create_incident, name="incidents/create"),
    path("delete/", views.delete_incidents, name="incidents/delete"),
    path("info/", views.incident_info, name="incidents/info"),
]
