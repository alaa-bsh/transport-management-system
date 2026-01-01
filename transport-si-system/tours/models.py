from django.db import models
from logistics.models import Driver, Vehicle

class Tour(models.Model):
    date = models.DateField()
    driver = models.ForeignKey(
        Driver,
        on_delete=models.PROTECT,
        related_name='tours'
    )
    vehicle = models.ForeignKey(
        Vehicle,
        on_delete=models.PROTECT,
        related_name='tours'
    )

    distance_km = models.FloatField(null=True, blank=True)
    duration_hours = models.FloatField(null=True, blank=True)
    fuel_consumption = models.FloatField(null=True, blank=True)

    status = models.CharField(
        max_length=50,
        choices=[
            ('planned', 'Planned'),
            ('in_progress', 'In Progress'),
            ('completed', 'Completed'),
            ('cancelled', 'Cancelled'),
        ],
        default='planned'
    )

    notes = models.TextField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Tour {self.id} - {self.date}"
