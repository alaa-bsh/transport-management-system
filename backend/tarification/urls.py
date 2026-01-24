from django.urls import path
from . import views

urlpatterns = [
    path('', views.tarification_data, name="tarifications"),
    path('<int:tarification_id>/', views.tarification_id_view, name="tarifications/id"),
    path('<int:tarification_id>/edit/', views.update_tarification, name="tarifications/edit"),
    path('create/', views.create_tarification, name="tarifications/create"),
    path('delete/', views.delete_tarifications, name="tarifications/delete"),
    path('info/', views.tarification_info, name="tarifications/info"),
]
