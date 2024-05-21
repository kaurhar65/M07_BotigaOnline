from rest_framework import serializers
from .models import Carreto

class CarretoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Carreto
        fieelds = '__all__'