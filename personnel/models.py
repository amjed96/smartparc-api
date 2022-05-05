from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):
    
    cin = models.IntegerField(null=True, blank=True)
    #first_name = models.CharField(max_length=255) EXISTS
    #last_name = models.CharField(max_length=255) EXISTS
    date_naissance = models.DateField(null=True, blank=True)
    telephone = models.IntegerField(null=True, blank=True)
    #email = models.EmailField() EXISTS
    #mot_de_passe = models.CharField(max_length=255) EXISTS
    qualification = models.CharField(max_length=255,null=True, blank=True)
    type_permis = models.CharField(max_length=255,null=True, blank=True)
    username = models.CharField(max_length=25,null=True,unique=True, blank=True)
    password = models.CharField(max_length=25,null=True, blank=True)
    
class Permis(models.Model):

    reference = models.CharField(max_length=10, primary_key=True)
    date = models.DateField(blank=True)
    personnel = models.ForeignKey('personnel.User', null=True, on_delete=models.CASCADE, related_name='permis_personnel', blank=True)
    type = models.CharField(max_length=10, blank=True)
    
class Passeport(models.Model):

    numero = models.CharField(max_length=25, primary_key=True)
    type = models.CharField(max_length=25, blank=True)
    personnel = models.ForeignKey('personnel.User', null=True, on_delete=models.CASCADE, related_name='passeport_personnel', blank=True)
    nationalite = models.CharField(max_length=25, blank=True)
    adresse_naissance = models.CharField(max_length=25, blank=True)
    sexe = models.CharField(max_length=25, blank=True)
    authorite_edition = models.CharField(max_length=25, blank=True)
    date_edition = models.DateField(blank=True)
    date_expiration = models.DateField(blank=True)
    
class Visite(models.Model):
    
    personnel = models.ForeignKey('personnel.User', on_delete=models.CASCADE, related_name='visites_personnel', blank=True)
    date = models.DateField(blank=True)
    diagnostique = models.TextField(max_length=255, blank=True)
    num_ordonnance = models.CharField(max_length=25, blank=True)