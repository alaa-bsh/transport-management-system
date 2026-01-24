from django.urls import path
from . import views

urlpatterns = [
    path('', views.typeservice_data, name="typeservice"),
    path('<int:service_id>/', views.typeservice_id_view, name="typeservice/id"),
    path('<int:service_id>/edit/', views.update_typeservice, name='typeservice/edit'),
    path("create/", views.create_typeservice, name="typeservice/create"),
    path("delete/", views.delete_typeservices, name="typeservice/delete"),
    path("info/", views.typeservice_info, name="typeservice/info"),
]
