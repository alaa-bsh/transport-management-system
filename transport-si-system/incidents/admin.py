from django.contrib import admin
from .models import Incident

@admin.register(Incident)
class IncidentAdmin(admin.ModelAdmin):
    list_display = ('incident_type', 'tour', 'resolved', 'date_reported')
    list_filter = ('incident_type', 'resolved')
    search_fields = ('description',)
