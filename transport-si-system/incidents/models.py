from django.db import models
from manageExpedition.models import Tournee

class Incident(models.Model):
    TYPE_INCIDENTS = [
         ('retard', 'Retard'),
        ('perte', 'Perte'),
        ('dommage', 'Dommage'),
        ('technique', 'Problème technique'),
        ('autre', 'Autre'),
    ]
    incident_type = models.CharField(max_length=50,choices=TYPE_INCIDENTS)
    tour = models.ForeignKey(Tournee,on_delete=models.SET_NULL,null=True,related_name='incidents')
    description = models.TextField()
    date_reported = models.DateTimeField(auto_now_add=True)
    resolu = models.BooleanField(default=False)

    def __str__(self):
        return self.incident_type + '-' + self.tour_id

