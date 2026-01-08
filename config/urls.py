"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path , include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('clients/', include('backend.clients.urls'), name='clients'),
    # path("chauffeur/", include('backend.logistics.urls')),
    # path("vehicule/", include('backend.logistics.urls')),
    path("destination/", include('backend.manageDestination.urls')),
    # path("type_service/", views.type_service_view, name="type_service"),
    # path colis
    # path("tarification/", views.tarification_view, name="tarification"),
    path("expedition/", include('backend.manageExpedition.urls')),
    path("tournee/", include('backend.manageExpedition.urls')),
    path("facturation/", include('backend.manageExpedition.urls')),
    # path("paiement/", views.facturation_view, name="paiement"),
    # path("incident/", views.incident_view, name="incident"),
    # path("reclamation/", include('backend.reclamations.urls')),
]
