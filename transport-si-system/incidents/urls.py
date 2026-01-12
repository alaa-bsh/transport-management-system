from django.urls import path
from .views import incident_list

urlpatterns = [
    path('', incident_list),
]
