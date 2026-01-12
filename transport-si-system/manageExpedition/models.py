from django.db import models    
from clients.models import Client 
from manageDestination.models import Destination
from logistics.models import Chauffeur
from logistics.models import Vehicule







class Tournee(models.Model) : 
    date_tournee = models.DateField()
    chauffeur = models.ForeignKey(Chauffeur , on_delete=models.SET_NULL , null=True)
    vehicule = models.ForeignKey(Vehicule , on_delete=models.SET_NULL, null=True)
    destinations = models.ManyToManyField(Destination , related_name="Tournee")

    def __str__(self):
        return f"Tournee #{self.id}"


class Facture (models.Model) :
    client = models.ForeignKey( Client,on_delete=models.CASCADE,related_name="factures",  null=True,blank=True)
    date_fact = models.DateField(auto_now=True)
    #reclamation = models.OneToOneField(Reclamation , on_delete=models.CASCADE)

    @property
    def montant_HT(self):
       exps = self.client.expeditions.all()
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
        ('trsit','en transit'),
        ('centri','en centre de tri'),
        ('encourslivr','en cours de livraison '),
        ('livr','livré'),
        ('echec','echec de livraison'),
    ]
    id_Exp = models.CharField(max_length=10 , primary_key=True , default="JHY-52")
    client = models.ForeignKey(Client, on_delete=models.CASCADE  ,null=True,blank=True)
    #id_service = models.ForeignKey(typeService , on_delete=models.CASCADE)
    statut = models.CharField( max_length=20 ,choices=STATUT )
    date_exped = models.DateTimeField(auto_now=True)
    #tarification = models.ForeignKey(Tarification , on_delete=models.CASCADE)
    numBureau = models.ForeignKey(Destination , on_delete=models.CASCADE)
    tournee = models.ForeignKey(Tournee,on_delete=models.SET_NULL,null=True,blank=True,related_name="expeditions")
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





