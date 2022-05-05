from django.shortcuts import render
from rest_framework import viewsets
from .serializers import VehiculeSerializer, AffectationSerializer, ContratLocationSerializer, ContratAchatSerializer, ConsommationSerializer

from .models import Vehicule, Affectation, ContratLocation, ContratAchat, Consommation

# Create your views here.


class VehiculeViewset(viewsets.ModelViewSet):
    queryset = Vehicule.objects.all()
    serializer_class = VehiculeSerializer
    
    def __str__(self):
        return self.name
    
class AffectationViewset(viewsets.ModelViewSet):
    queryset = Affectation.objects.all()
    serializer_class = AffectationSerializer
    
    def __str__(self):
        return self.name
    
class ContratLocationFlotteViewset(viewsets.ModelViewSet):
    queryset = ContratLocation.objects.all()
    serializer_class = ContratLocationSerializer
    
    def __str__(self):
        return self.name
    
class ContratAchatViewset(viewsets.ModelViewSet):
    queryset = ContratAchat.objects.all()
    serializer_class = ContratAchatSerializer
    
    def __str__(self):
        return self.name
    
class ConsommationViewset(viewsets.ModelViewSet):
    queryset = Consommation.objects.all()
    serializer_class = ConsommationSerializer
    
    def __str__(self):
        return self.name