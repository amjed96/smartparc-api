from django.shortcuts import render
from rest_framework import viewsets

from .models import Permis, Passeport, Visite, User
from .serializers import UserSerializer, PermisSerializer, PasseportSerializer, VisiteSerializer

#from models import Permis

# Create your views here.


class UserViewset(viewsets.ModelViewSet): ##### TO DO #####
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
    def __str__(self):
        return self.name
    
class PermisViewset(viewsets.ModelViewSet):
    queryset = Permis.objects.all()
    serializer_class = PermisSerializer
    
    def __str__(self):
        return self.name
    
class PasseportViewset(viewsets.ModelViewSet):
    queryset = Passeport.objects.all()
    serializer_class = PasseportSerializer
    
    def __str__(self):
        return self.name
    
class VisiteViewset(viewsets.ModelViewSet):
    queryset = Visite.objects.all()
    serializer_class = VisiteSerializer
    
    def __str__(self):
        return self.name