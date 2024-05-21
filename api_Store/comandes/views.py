from django.shortcuts import render
from .serializer import *
from .models import *
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.
@api_view(['GET'])
def get_Comand(request):
    comandList = Comanda.objects.all()
    data_serializer = comandaSerializer(comandList, many=True)
    return Response({"data":data_serializer.data})

@api_view(['GET'])
def get_Comand_ById(request, pk):
    comandList = Comanda.objects.get(id=pk)
    data_serializer = comandaSerializer(comandList, many=False)
    return Response({"data":data_serializer.data})

@api_view(['DELETE'])
def delete_Comand_ById(request, pk):
    comand= Comanda.objects.get(id=pk)
    comand.delete()
    return Response({"message": "oleeeee eliminado"})
