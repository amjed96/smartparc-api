from django.shortcuts import render
from rest_framework import viewsets
from .serializers import DossierVoyageSerializer, FicheTrajetSerializer

from  .models import DossierVoyage, FicheTrajet

# Create your views here.


class DossierVoyageViewset(viewsets.ModelViewSet):
    queryset = DossierVoyage.objects.all()
    serializer_class = DossierVoyageSerializer
    
class FicheTrajetViewset(viewsets.ModelViewSet):
    queryset = FicheTrajet.objects.all()
    serializer_class = FicheTrajetSerializer