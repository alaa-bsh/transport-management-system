from django.urls import path
from . import views

urlpatterns = [
    path('', views.colis_data, name="colis"),
    path('<int:colis_id>/', views.colis_id_view, name="colis/id"),
    path('<int:colis_id>/edit/', views.update_colis, name='colis/edit'),
    path("create/", views.create_colis, name="colis/create"),
    path("delete/", views.delete_colis, name="colis/delete"),
    path("info/", views.colis_info, name="colis/info"),
]
