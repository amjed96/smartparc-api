from django.shortcuts import render
from rest_framework import viewsets
from .serializers import ContratLocationSerializer

from .models import ContratLocation

# Create your views here.


class ContratLocationViewset(viewsets.ModelViewSet):
    queryset = ContratLocation.objects.all()
    serializer_class = ContratLocationSerializer
    
    def __str__(self):
        return self.name