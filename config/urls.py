from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('clients/', include('backend.clients.urls')),
    path('colis/', include('backend.manageColis.urls')),
    path('chauffeurs/', include('backend.logistics.chauf_urls')),
    path('vehicules/', include('backend.logistics.veh_urls')),
    path('destinations/', include('backend.manageDestination.urls')),
    path('typeservice/', include('backend.typeservice.urls')),
    path('tarification/', include('backend.tarification.urls')),
    path('expeditions/', include('backend.manageExpedition.Exp_urls')),
    path('tournees/', include('backend.manageExpedition.Tour_urls')),
    path('factures/', include('backend.manageExpedition.Fac_urls')),
    path('incidents/', include('backend.incidents.urls')),
    path('reclamations/', include('backend.reclamations.urls')),
    path('dashboard/', include('backend.dashboard.urls')),
]
