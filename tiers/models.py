from django.db import models

# Create your models here.


class Tiers(models.Model):
    
    compte = models.CharField(max_length=25)
    intitule = models.CharField(max_length=25)
    abrege = models.CharField(max_length=25)
    compte_collectif = models.CharField(max_length=25)
    qualite = models.CharField(max_length=25)
    interlocuteur = models.CharField(max_length=25)
    commentaire = models.TextField(max_length=255)
    type = models.BooleanField()
    
class Contact(models.Model):
    
    tiers = models.ForeignKey('tiers.Tiers', null=True, on_delete=models.SET_NULL, related_name='contacts_tiers')
    type = models.CharField(max_length=25)
    civilite = models.CharField(max_length=25)
    nom = models.CharField(max_length=25)
    prenom = models.CharField(max_length=25)
    service = models.CharField(max_length=25)
    fonction = models.CharField(max_length=25)
    telephone = models.CharField(max_length=25)
    portable = models.CharField(max_length=25)
    telecopie = models.CharField(max_length=25)
    skype = models.CharField(max_length=25)
    linkedin = models.CharField(max_length=25)
    facebook = models.CharField(max_length=25)
    email = models.EmailField()