from django.db import models

# Create your models here.


class Document(models.Model):
    
    type = models.CharField(max_length=25)
    date = models.DateField()
    numero = models.CharField(max_length=25)
    tiers = models.ForeignKey('tiers.Tiers', null=True, on_delete=models.SET_NULL, related_name='documents_tiers')
    
class DemandeAchat(models.Model):
    
    date = models.DateField()
    demandeur = models.ForeignKey('personnel.User', null=True, on_delete=models.SET_NULL, related_name='personnel_demande_achat')
    article = models.CharField(max_length=25)
    nombre = models.IntegerField()
    description = models.TextField(max_length=255)
    statut = models.CharField(max_length=25)
    
class Stock(models.Model):
    
    reference = models.CharField(max_length=25, primary_key=True)
    article = models.CharField(max_length=25)
    codecasier = models.CharField(max_length=25)
    dateachat = models.DateField()
    quantite = models.IntegerField()
    unite = models.CharField(max_length=25)