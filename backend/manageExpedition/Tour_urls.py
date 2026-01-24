from django.urls import path
from . import Tour_views as views

urlpatterns = [
    path('', views.tournee_data, name="tournees"),
    path('<int:tournee_id>/', views.tournee_id_view, name="tournees/id"),
    path('<int:tournee_id>/edit/', views.update_tournee, name='tournees/edit'),
    path("create/", views.create_tournee, name="tournees/create"),
    path("delete/", views.delete_tournees, name="tournees/delete"),
    path("info/", views.tournee_info, name="tournees/info"),
]
