from django.shortcuts import render
from rest_framework import viewsets
from .serializers import TiersSerializer, ContactSerializer

from .models import Tiers, Contact

# Create your views here.


class TiersViewset(viewsets.ModelViewSet):
    queryset = Tiers.objects.all()
    serializer_class = TiersSerializer
    
class ContactViewset(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer