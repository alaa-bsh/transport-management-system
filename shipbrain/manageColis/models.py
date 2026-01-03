from django.db import models

# Create your models here.

class Colis (models.Model) :
    poids = models.FloatField(max_length=10)
    volume = models.FloatField(max_length=10)
    description = models.CharField(max_length=100)
    expedition = models.ForeignKey('manageExpedition.Expedition', on_delete=models.CASCADE)

    def __str__(self):
        return self.description
