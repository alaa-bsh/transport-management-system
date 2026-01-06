from django.db import models
from django.utils import timezone

# Create your models here.
class Product(models.Model):
    id_prd = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    price = models.FloatField(max_length=10)
    created_at = models.DateTimeField(auto_now=True)


class Client(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    telephone = models.CharField(max_length=20)
    email = models.EmailField(unique=True)
    solde = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    date_creation = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nom} {self.prenom}"