from django.shortcuts import render
from rest_framework import viewsets
from .serializers import DemandeInterventionSerializer, InterventionSerializer, PieceRechangeSerializer, PlanEntretienSerializer

from .models import DemandeIntervention, Intervention, PieceRechange, PlanEntretien

# Create your views here.


class DemandeInterventionViewset(viewsets.ModelViewSet):
    queryset = DemandeIntervention.objects.all()
    serializer_class = DemandeInterventionSerializer
    
    def __str__(self):
        return self.name
    
class InterventionViewset(viewsets.ModelViewSet):
    queryset = Intervention.objects.all()
    serializer_class = InterventionSerializer
    
    def __str__(self):
        return self.name
    
class PieceRechangeViewset(viewsets.ModelViewSet):
    queryset = PieceRechange.objects.all()
    serializer_class = PieceRechangeSerializer
    
    def __str__(self):
        return self.name
    
class PlanEntretienViewset(viewsets.ModelViewSet):
    queryset = PlanEntretien.objects.all()
    serializer_class = PlanEntretienSerializer
    
    def __str__(self):
        return self.name