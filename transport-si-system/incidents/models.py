from django.db import models

class Incident(models.Model):
    TYPE_CHOICES = [
        ('retard', 'Retard'),
        ('perte', 'Perte'),
        ('dommage', 'Endommagement'),
        ('technique', 'Problème technique'),
    ]

    type_incident = models.CharField(max_length=20, choices=TYPE_CHOICES)
    description = models.TextField()
    date_incident = models.DateTimeField(auto_now_add=True)
    resolu = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.type_incident} - {self.date_incident.date()}"
