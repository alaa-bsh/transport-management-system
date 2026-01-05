from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('manageExpedition/', include('manageExpedition.urls')),
    path('manageDestination/', include('manageDestination.urls')),
    path('manageColis/', include('manageColis.urls')),
    
]