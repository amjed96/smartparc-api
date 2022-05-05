from django.db import models

# Create your models here.


class DemandeIntervention(models.Model):
    
    date_demande = models.DateField()
    vehicule = models.ForeignKey('flotte.Vehicule', null=True, on_delete=models.SET_NULL, related_name='demande_vehicule')
    type = models.CharField(max_length=25)
    description = models.TextField(max_length=255)
    etat = models.CharField(max_length=25)
    
class Intervention(models.Model):
    
    vehicule = models.ForeignKey('flotte.Vehicule', null=True, on_delete=models.SET_NULL, related_name='intervention_vehicule')
    date_debut = models.DateField()
    date_fin = models.DateField()
    objet = models.CharField(max_length=25)
    entreprise = models.CharField(max_length=25)
    montant_mo_ht = models.IntegerField()
    montant_pieces_ht = models.IntegerField()
    montant_total_ht = models.IntegerField()
    collaborateur = models.CharField(max_length=25)
    
class PieceRechange(models.Model):
    
    code = models.CharField(max_length=25, primary_key=True)
    nom = models.CharField(max_length=25)
    code_casier = models.CharField(max_length=25)
    famille = models.CharField(max_length=25)
    categorie = models.CharField(max_length=25)
    unite = models.CharField(max_length=25)
    prix = models.IntegerField()
    nombre = models.IntegerField()
    
class PlanEntretien(models.Model):
    
    operation = models.CharField(max_length=25)
    vehicule = models.ForeignKey('flotte.Vehicule', null=True, on_delete=models.SET_NULL, related_name='plan_vehicule')
    type = models.CharField(max_length=25)
    frequence = models.IntegerField()
    unite = models.CharField(max_length=25)