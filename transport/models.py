from django.db import models

# Create your models here.


class DossierVoyage(models.Model):
    
    code = models.CharField(max_length=25, primary_key=True)    
    numero = models.IntegerField()
    ref_aller = models.IntegerField()
    date_creation = models.DateField()
    chauffeur = models.ForeignKey('personnel.User', null=True, on_delete=models.SET_NULL, related_name='dossiers_voyage_personnel')
    vehicule = models.ForeignKey('flotte.Vehicule', null=True, on_delete=models.SET_NULL, related_name='dossiers_voyage_vehicule')
    remorque = models.CharField(max_length=25)
    client = models.ForeignKey('tiers.Tiers', null=True, on_delete=models.SET_NULL, related_name='dossiers_voyage_client')
    voyage = models.CharField(max_length=25)
    date_chargement = models.DateField()
    date_dechargement = models.DateField()
    montant_ht = models.IntegerField()
    etat = models.CharField(max_length=25)
    
class FicheTrajet(models.Model):
    
    nom = models.CharField(max_length=25)
    client = models.ForeignKey('tiers.Tiers', null=True, on_delete=models.SET_NULL, related_name='fiche_trajet_tiers')
    marchandise = models.CharField(max_length=25)
    trajet = models.CharField(max_length=25)
    unite = models.CharField(max_length=25)
    type_prestation = models.CharField(max_length=25)
    categorie = models.CharField(max_length=25)
    date_debut = models.DateField()
    date_fin = models.DateField()
    prix = models.IntegerField()
    prix_retour = models.IntegerField()