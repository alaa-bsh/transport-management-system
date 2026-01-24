from django.urls import path
from . import Exp_views as views

urlpatterns = [
    path('', views.expedition_data, name="expeditions"),
    path('<int:expedition_id>/', views.expedition_id_view, name="expeditions/id"),
    path('<int:expedition_id>/edit/', views.update_expedition, name='expeditions/edit'),
    path("create/", views.create_expedition, name="expeditions/create"),
    path("delete/", views.delete_expeditions, name="expeditions/delete"),
    path("info/", views.expedition_info, name="expeditions/info"),
]
