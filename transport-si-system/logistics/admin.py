from django.contrib import admin
from .models import Driver, Vehicle

@admin.register(Driver)
class DriverAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'license_number', 'available')
    search_fields = ('first_name', 'last_name', 'license_number')


@admin.register(Vehicle)
class VehicleAdmin(admin.ModelAdmin):
    list_display = ('plate_number', 'vehicle_type', 'capacity', 'status')
    search_fields = ('plate_number',)
