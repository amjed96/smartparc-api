from django.db import models

# Create your models here.


class ContratLocation(models.Model):
    
    immatriculation = models.CharField(max_length=25)
    date_debut = models.DateField()
    date_fin = models.DateField()
    marque = models.CharField(max_length=25)
    modele = models.CharField(max_length=25)
    prix = models.IntegerField()