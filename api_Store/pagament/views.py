from django.shortcuts import render
from .serializer import *
from .models import *
from comandes.models import Comanda
from pagament.models import Pagament
from rest_framework.decorators import api_view
from rest_framework.response import Response


# Create your views here.
# ----------- retorna només l'estat de CADA COMANDA.  
@api_view(['GET'])
def get_Status_ById(request, comanda_id):
    try:
        comanda = Comanda.objects.get(id=comanda_id)
        data_serializer = comandaActiuSerializer(comanda)
        if comanda.actiu: return Response({"message": "Comanda no pagada", "data": data_serializer.data})
        else:
            return Response({"message": "Comanda pagada", "data": data_serializer.data})
    except Comanda.DoesNotExist:
        return Response({"error": "Comanda no trobada"})
    

# ----------- pagar comanda a través de app pagament.
@api_view(['POST'])
def pay_Comand(request, comanda_id):
    try:
        comanda = Comanda.objects.get(id=comanda_id)
        if comanda.actiu == False:
            return Response({"error": "La comanda ja està pagada"})
        
        # Crear un nou pagament
        data = request.data
        pagament = Pagament(
            comanda=comanda,
            numTarjeta=data['numTarjeta'],
            dataCad=data['dataCad'],
            cvc=data['cvc'],
            actiu= False
        )
        pagament.save()
        # ja ha pagat, comanda inactiva.
        comanda.actiu = False
        comanda.save()
        
        data_serializer = payComandSerializer(pagament)
        return Response({"message": "Comanda pagada amb èxit", "data": data_serializer.data})
    except Comanda.DoesNotExist:
        return Response({"error": "Comanda no trobada"})
