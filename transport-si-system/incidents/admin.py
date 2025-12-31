from django.contrib import admin
from .models import Incident

@admin.register(Incident)
class IncidentAdmin(admin.ModelAdmin):
    list_display = ('type_incident', 'date_incident', 'resolu')
    list_filter = ('type_incident', 'resolu')
    search_fields = ('description',)
