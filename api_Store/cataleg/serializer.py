from rest_framework import serializers
from .models import *

class producteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producte
        fieelds = '__all__'

class catalagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cataleg
        fieelds = '__all__'