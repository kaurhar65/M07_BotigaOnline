from rest_framework import serializers
from .models import *

class clientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fieelds = '__all__'