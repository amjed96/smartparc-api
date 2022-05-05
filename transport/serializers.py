from rest_framework import serializers

from .models import DossierVoyage, FicheTrajet


class DossierVoyageSerializer(serializers.ModelSerializer):
    class Meta:
        model = DossierVoyage
        fields = '__all__'
        
class FicheTrajetSerializer(serializers.ModelSerializer):
    class Meta:
        model = FicheTrajet
        fields = '__all__'