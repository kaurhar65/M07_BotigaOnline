from django.shortcuts import render
from .serializer import *
from .models import *
from comandes.models import Comanda
from rest_framework.decorators import api_view
from rest_framework.response import Response


# Create your views here.
# ----------- retorna només les comandes obertes 
@api_view(['GET'])
def get_Comand_Status(request, comanda_id):
    try:
        comanda = Comanda.objects.get(id=comanda_id, actiu=True)
        data_serializer = comandaSerializer(comanda)
        return Response({"data": data_serializer.data})
    except Comanda.DoesNotExist:
        return Response({"error": "Comanda no trobada"})
    

# ----------- pagar comanda a través de app pagament.
@api_view(['POST'])
def pay_Comand(request, comanda_id):
    try:
        comanda = Comanda.objects.get(id=comanda_id)
        if comanda.actiu:
            return Response({"error": "La comanda ja està pagada"})
        
        # Crear un nou pagament
        data = request.data
        pagament = Pagament(
            comanda=comanda,
            client=comanda.client,
            numTarjeta=data['numTarjeta'],
            dataCad=data['dataCad'],
            cvc=data['cvc']
        )
        pagament.save()

        # ja ha pagat, comanda inactiva.
        comanda.actiu = False
        comanda.save()
        
        data_serializer = comandaSerializer(comanda)
        return Response({"message": "Comanda pagada amb èxit", "data": data_serializer.data})
    except Comanda.DoesNotExist:
        return Response({"error": "Comanda no trobada"})