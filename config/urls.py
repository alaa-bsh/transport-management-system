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
    path('clients/', include('backend.clients.urls')),
    path('colis/', include('backend.manageColis.urls')),
    path("chauffeurs/", include('backend.logistics.chauf_urls')),
    path("vehicules/", include('backend.logistics.veh_urls')),
    path("destinations/", include('backend.manageDestination.urls')),
    path("typeservice/", include('backend.typeservice.urls')),
    path("colis/", include('backend.manageColis.urls')),
    path("tarification/", include('backend.tarification.urls')),
    path("Expeditions/", include('backend.manageExpedition.Exp_urls')),
    path("Tournees/", include('backend.manageExpedition.Tour_urls')),
    path("Factures/", include('backend.manageExpedition.Fac_urls')),
    # path("paiement/", views.facturation_view, name="paiement"),
    path("Incidents/", include('backend.incidents.urls')),
    path("reclamations/", include('backend.reclamations.urls')),
    #path("dashboard/", include('backend.dashboard.urls')),
]
