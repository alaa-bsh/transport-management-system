from django.db import models

# Create your models here.

class Colis (models.Model) :
    poids = models.FloatField(max_length=10)
    volume = models.FloatField(max_length=10)
    description = models.CharField(max_length=100)
    id_exp = models.ForeignKey('manageExpedition.Expedition', max_length=10 , on_delete=models.CASCADE , default='JHY-52')

    def __str__(self):
        return f"#{self.id}"
