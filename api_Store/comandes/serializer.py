from rest_framework import serializers
from .models import *

class comandaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comanda
        fieelds = '__all__'