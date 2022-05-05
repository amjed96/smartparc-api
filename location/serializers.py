from rest_framework import serializers

from .models import ContratLocation


class ContratLocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContratLocation
        fields = '__all__'