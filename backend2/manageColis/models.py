from django.db import models
from backend.manageExpedition.models import Expedition

class Colis (models.Model) :
    poids = models.FloatField(max_length=10)
    volume = models.FloatField(max_length=10)
    description = models.CharField(max_length=100)
    expedition = models.ForeignKey(Expedition, max_length=10 , on_delete=models.CASCADE )

    def __str__(self):
        return f"#{self.id}"
