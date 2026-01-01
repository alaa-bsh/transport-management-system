from django.db import models
from clients.models import Client
from incidents.models import Incident

class Reclamation(models.Model):

    STATUT_CHOICES = [
        ('en_cours', 'En cours'),
        ('resolue', 'Résolue'),
        ('annulee', 'Annulée'),
    ]

    client = models.ForeignKey(
        Client,
        on_delete=models.CASCADE,
        related_name='reclamations'
    )

    incident = models.ForeignKey(
        Incident,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='reclamations'
    )

    objet = models.CharField(max_length=200)
    description = models.TextField()
    date_reclamation = models.DateTimeField(auto_now_add=True)
    statut = models.CharField(
        max_length=20,
        choices=STATUT_CHOICES,
        default='en_cours'
    )

    def __str__(self):
        return f"Réclamation #{self.id} - {self.client.nom}"
from django.db import models
from clients.models import Client
from incidents.models import Incident

class Reclamation(models.Model):

    STATUT_CHOICES = [
        ('en_cours', 'En cours'),
        ('resolue', 'Résolue'),
        ('annulee', 'Annulée'),
    ]

    client = models.ForeignKey(
        Client,
        on_delete=models.CASCADE,
        related_name='reclamations'
    )

    incident = models.ForeignKey(
        Incident,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='reclamations'
    )

    objet = models.CharField(max_length=200)
    description = models.TextField()
    date_reclamation = models.DateTimeField(auto_now_add=True)
    statut = models.CharField(
        max_length=20,
        choices=STATUT_CHOICES,
        default='en_cours'
    )

    def __str__(self):
        return f"Réclamation #{self.id} - {self.client.nom}"
