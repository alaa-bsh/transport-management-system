from django.urls import path
from .views import reclamation_list

urlpatterns = [
    path('', reclamation_list),
]
