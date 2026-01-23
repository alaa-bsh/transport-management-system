from django.db import models

class Chauffeur(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    numPermis = models.CharField(max_length=50, unique=True)
    Tel = models.CharField(max_length=20)
    Email = models.EmailField(unique=True)
    Disponibilite = models.BooleanField(default=True)
    # FIXED: Changed from 'Adress' to 'Adresse'
    Adresse = models.TextField()

    def __str__(self):
        return self.nom + '-'+ self.prenom

class Vehicule(models.Model):
    ETAT = [
            ('Dispo', 'Disponible'),
            ('maint', 'Maintenance'),
            ('onRoute', 'On Route'),
        ]
    numImmat = models.CharField(max_length=20, unique=True)
    type_vehicule = models.CharField(max_length=50)
    capacitePoids = models.FloatField()
    capaciteVolume = models.FloatField()
    consommationCarburant = models.FloatField()
    # FIXED: Changed default to match choices
    etat = models.CharField(max_length=50, choices = ETAT, default='Dispo')

    def __str__(self):
        return self.numImmat