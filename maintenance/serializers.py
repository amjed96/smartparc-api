from rest_framework import serializers

from .models import DemandeIntervention, Intervention, PieceRechange, PlanEntretien


class DemandeInterventionSerializer(serializers.ModelSerializer):
    class Meta:
        model = DemandeIntervention
        fields = '__all__'
        
class InterventionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Intervention
        fields = '__all__'
        
class PieceRechangeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PieceRechange
        fields = '__all__'
        
class PlanEntretienSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlanEntretien
        fields = '__all__'