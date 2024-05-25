from django.shortcuts import render
from .serializer import *
from .models import *
from rest_framework.decorators import api_view
from rest_framework.response import Response


# Create your views here.
@api_view(['GET'])
def get_Prod(request):
    productList = Producte.objects.all()
    data_serializer = producteSerializer(productList, many=True)
    return Response({"data":data_serializer.data})

@api_view(['GET'])
def get_Prod_ById(request, pk):
    productList = Producte.objects.get(id=pk)
    data_serializer = producteSerializer(productList, many=False)
    return Response({"data":data_serializer.data})

@api_view(['PUT'])
def delete_Prod_ById(request, pk):
    producte = Producte.objects.get(id=pk)
    producte.actiu = False
    producte.save()
    return Response({"message": "Producto eliminado correctamente"}, status=200)

@api_view(['POST'])
def add_Prod(request):
    serializer=producteSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

@api_view(['PUT'])
def update_Prod(request, pk):
    try:
        product = Producte.objects.get(pk=pk)
    except Producte.DoesNotExist:
        return Response({"error": "xisteeeee"}, status=404)

    serializer = producteSerializer(product, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=200)
    return Response(serializer.errors, status=400)

@api_view(['PUT'])
def editaStockProducte(request, pk):
    producte = Producte.objects.get(id=pk)
    serializer = producteQuantSerializer(producte, data=request.data)
    if serializer.is_valid():
        serializer.save()  
        return Response(serializer.data)
    return Response(serializer.errors, status=400)