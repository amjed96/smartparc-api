from rest_framework import serializers

from .models import Document, DemandeAchat, Stock


class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = '__all__'
        
class DemandeAchatSerializer(serializers.ModelSerializer):
    class Meta:
        model = DemandeAchat
        fields = '__all__'
        
class StockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stock
        fields = '__all__'