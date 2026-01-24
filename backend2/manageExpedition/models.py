from django.db import models    
from backend.typeservice.models import TypeService
from backend.manageDestination.models import Destination
from backend.logistics.models import Chauffeur
from backend.logistics.models import Vehicule


class Tournée(models.Model) : 
    dateTourne = models.DateField()
    id_chauff = models.ForeignKey(Chauffeur , on_delete=models.SET_NULL , null=True)
    id_vehicule = models.ForeignKey(Vehicule , on_delete=models.SET_NULL, null=True)
    numBureau = models.ManyToManyField(Destination , related_name="Tournee")

    def __str__(self):
        return f"Tournee #{self.id}"


class Facture (models.Model) :
    id_client = models.OneToOneField('clients.Client', on_delete=models.CASCADE)
    date_fact = models.DateField(auto_now=True)

    @property
    def montant_HT(self):
       exps = Expedition.objects.filter(id_client=self.id_client)
       montant_HT= 0 
       for e in exps :
           montant_exp = e.montant_total 
           montant_HT = montant_HT + montant_exp
       return montant_HT
    
    @property
    def montant_TTC(self):
       return (self.montant_HT * 0.19 ) + self.montant_HT



class Expedition(models.Model) :
    STATUT = [
        ('trsit','transit'),
        ('centri','en tri'),
        ('encourslivr','en cours '),
        ('livr','livré'),
        ('echec','echec'),
    ]
    id_client = models.ForeignKey('clients.Client', on_delete=models.CASCADE)
    service = models.ForeignKey(TypeService , on_delete=models.CASCADE , null=True)
    statut = models.CharField( max_length=20 ,choices=STATUT )
    date_exped = models.DateTimeField(auto_now=True)
    #tarification = models.ForeignKey(Tarification , on_delete=models.CASCADE)
    numBureau = models.ForeignKey(Destination , on_delete=models.CASCADE)
    id_tournée = models.ForeignKey(Tournée, on_delete=models.SET_NULL,null=True)
    @property
    def montant_total(self):
        tarifBase = self.numBureau.tarifBase
        poidsTot = 0
        volumeTot = 0
        for colis in self.id_colis.all():
            poidsTot  = poidsTot + colis.poids
            volumeTot = volumeTot + colis.volume
        prixPoidsTot = poidsTot * self.tarification.tarifPoids
        prixVolTot= volumeTot * self.tarification.tarifVol
        return tarifBase + prixPoidsTot + prixVolTot

    def __str__(self):
        return f"#{self.id_Exp}"





