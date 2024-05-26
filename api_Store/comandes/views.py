from django.shortcuts import render
from .serializer import *
from .models import *
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.
@api_view(['GET'])
def get_Comand(request):
    try:
        comandList = Comanda.objects.all()
        data_serializer = comandaSerializer(comandList, many=True)
        return Response({"message": "Totes les comandes", "data":data_serializer.data}, status=200)
    except Comanda.DoesNotExist:
        return Response({"message": "No hi han comandes registrades.", "data":data_serializer.data}, status=404)

@api_view(['GET'])
def get_Comand_ById(request, pk):
    try:
        comandList = Comanda.objects.get(id=pk)
        data_serializer = comandaSerializer(comandList, many=False)
        return Response({"message": "Comandes segons l'ID: ", "data":data_serializer.data})
    except Comanda.DoesNotExist:
        return Response({"message": "No hi ha cap comanda amb l'ID corresponent.", "data":data_serializer.data}, status=404)

@api_view(['GET'])
def get_Comand_ByClient(request, client_id):
    try:
        client = Client.objects.get(id=client_id)
        comandes = Comanda.objects.filter(client=client)
        data_serializer = comandaSerializer(comandes, many=True)
        return Response({"message": "Comandes segons l'ID client: ", "data": data_serializer.data}, status=200)
    except Client.DoesNotExist:
        return Response({"error": "Client no trobat."}, status=404)
    
@api_view(['GET'])
def get_Comand_Active(request):
    try:
        comandes = Comanda.objects.filter(actiu=True)
        data_serializer = comandaSerializer(comandes, many=True)
        return Response({"message": "Comandes que es troben actives: ", "data": data_serializer.data}, status=200)
    except Comanda.DoesNotExist:
        return Response({"error": "Totes les comandes estan pagades."}, status=404)

@api_view(['DELETE'])
def delete_Comand_ById(request, pk):
    try:
        comand= Comanda.objects.get(id=pk)
        comand.delete()
        return Response({"message": "Comanda eliminada correctament."}, status=200)
    except Comanda.DoesNotExist:
        return Response({"error": "Totes les comandes estan pagades."}, status=404)
