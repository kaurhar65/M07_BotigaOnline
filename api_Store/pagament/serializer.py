from rest_framework import serializers
from .models import *
from comandes.models import Comanda
        
class comandaActiuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comanda
        fields = ['actiu']

class payComandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pagament
        fields = ['numTarjeta', 'dataCad', 'cvc']