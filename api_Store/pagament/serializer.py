from rest_framework import serializers
from .models import *
from comandes.models import Comanda

class pagamentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pagament
        fields = '__all__'
        
class comandaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comanda
        fields = '__all__'
        
class comandaActiuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comanda
        fields = ['actiu']