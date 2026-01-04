from django.db import models

# Create your models here.
class Destination (models.Model) :
    numBureau = models.IntegerField(primary_key=True)
    ville = models.CharField(max_length=30)
    pays = models.CharField(max_length=20)
    zoneGeo = models.CharField(max_length=30)
    tarifBase = models.FloatField(max_length=10)

    def __str__(self):
        return self.ville + " - " + self.pays + " - " + self.zoneGeo
