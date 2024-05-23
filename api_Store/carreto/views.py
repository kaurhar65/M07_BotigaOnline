from django.shortcuts import render
from .serializer import *
from .models import *
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.
@api_view(['GET'])
def get_Carreto(request):
    carretoList = Carreto.objects.all()
    data_serializer = CarretoSerializer(carretoList, many=True)
    return Response({"data":data_serializer.data})

@api_view(['GET'])
def get_Carreto_ById(request, pk):
    carreto = Carreto.objects.get(id=pk)
    data_serializer = CarretoSerializer(carreto, many=False)
    return Response({"data":data_serializer.data})

@api_view(['DELETE'])
def delete_Carreto_ById(request, pk):
    carreto= Carreto.objects.get(id=pk)
    carreto.delete()
    return Response({"message": "oleeeee eliminado"})