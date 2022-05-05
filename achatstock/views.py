from django.shortcuts import render
from rest_framework import viewsets
from .serializers import DocumentSerializer, DemandeAchatSerializer, StockSerializer

from  .models import Document, DemandeAchat, Stock

# Create your views here.


class DocumentViewset(viewsets.ModelViewSet):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer
    
    def __str__(self):
        return self.name
    
class DemandeAchatViewset(viewsets.ModelViewSet):
    queryset = DemandeAchat.objects.all()
    serializer_class = DemandeAchatSerializer
    
    def __str__(self):
        return self.name
    
class StockViewset(viewsets.ModelViewSet):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer
    
    def __str__(self):
        return self.name