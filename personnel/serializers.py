from rest_framework import serializers
from django.contrib.auth import get_user_model

from .models import Permis, Passeport, Visite


class UserSerializer(serializers.ModelSerializer): ##### TO DO #####
    class Meta:
        User = get_user_model()
        model = User
        fields = '__all__'
        
class PermisSerializer(serializers.ModelSerializer):
    class Meta:
        model = Permis
        fields = '__all__'
        
class PasseportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Passeport
        fields = '__all__'
        
class VisiteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Visite
        fields = '__all__'