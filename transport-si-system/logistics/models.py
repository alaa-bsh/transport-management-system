from django.db import models

class Driver(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    license_number = models.CharField(max_length=50, unique=True)
    phone = models.CharField(max_length=20)
    available = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Vehicle(models.Model):
    plate_number = models.CharField(max_length=20, unique=True)
    vehicle_type = models.CharField(max_length=50)
    capacity = models.FloatField(help_text="Capacity in kg")
    consumption = models.FloatField(help_text="Fuel consumption per 100km")
    status = models.CharField(
        max_length=50,
        choices=[
            ('available', 'Available'),
            ('maintenance', 'Maintenance'),
            ('on_route', 'On Route'),
        ],
        default='available'
    )

    def __str__(self):
        return self.plate_number
