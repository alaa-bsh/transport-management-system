from django.db import models
from tours.models import Tour

class Incident(models.Model):

    INCIDENT_TYPES = [
        ('delay', 'Delay'),
        ('loss', 'Loss'),
        ('damage', 'Damage'),
        ('technical', 'Technical problem'),
        ('other', 'Other'),
    ]

    incident_type = models.CharField(
        max_length=50,
        choices=INCIDENT_TYPES
    )

    tour = models.ForeignKey(
        Tour,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='incidents'
    )

    description = models.TextField()
    date_reported = models.DateTimeField(auto_now_add=True)

    resolved = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.incident_type} - Tour {self.tour_id}"
