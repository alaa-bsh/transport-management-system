from django.urls import path
from . import views

urlpatterns = [
    path('analyse_commerciale', views.dashboard, name="dashboard_commerciale"),
    path('analyse_operationelle', views.dashboard, name="dashboard_operationelle"),
]
