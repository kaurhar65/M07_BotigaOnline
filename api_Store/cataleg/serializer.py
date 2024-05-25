from rest_framework import serializers
from .models import *

class producteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producte
        fields = '__all__'

class catalagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cataleg
        fields = '__all__'

class producteQuantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producte
        fields = ['quantitat']