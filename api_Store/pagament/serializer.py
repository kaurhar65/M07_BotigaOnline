from rest_framework import serializers
from .models import *

class pagamentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pagament
        fieelds = '__all__'