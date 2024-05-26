from django.shortcuts import render
from .serializer import *
from .models import *
from rest_framework.decorators import api_view
from rest_framework.response import Response


# Create your views here.
@api_view(['GET'])
def get_Prod(request):
    try: 
        productList = Producte.objects.all()
        data_serializer = producteSerializer(productList, many=True)
        return Response({"message:":"Tots els productes", "data":data_serializer.data})
    except Producte.DoesNotExist:
        return Response({"error": "No hi han productes registrats."}, status=404)


@api_view(['GET'])
def get_Prod_ById(request, pk):
    try:
        productList = Producte.objects.get(id=pk)
        data_serializer = producteSerializer(productList, many=False)
        return Response({"message:":"Producte segons l'ID","data":data_serializer.data})
    except Producte.DoesNotExist:
        return Response({"error": "No existeix aquest ID."}, status=404)

@api_view(['PUT'])
def delete_Prod_ById(request, pk):
    try: 
        producte = Producte.objects.get(id=pk)
        producte.actiu = False
        producte.save()
        return Response({"message:":"Producte eliminat correctament."}, status=200)
    except Producte.DoesNotExist:
        return Response({"error": "No existeix aquest producte."}, status=404)

@api_view(['POST'])
def add_Prod(request):
    try:
        serializer=producteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({ "message:":" Producte afegit correctament", "data":serializer.data},status=201)
    except:
        return Response({"error": "No s'ha pogut completar l'acció", "data":serializer.errors}, status=400)

@api_view(['PUT'])
def update_Prod(request, pk):
    try:
        product = Producte.objects.get(pk=pk)
    except Producte.DoesNotExist:
        return Response({"error": "No existeix aquest producte."}, status=404)

    serializer = producteSerializer(product, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({ "message:":" Producte actualitzat correctament", "data":serializer.data}, status=200)
    return Response({"error": "No s'ha pogut actualitzar l'informació", "data":serializer.errors}, status=400)

@api_view(['PUT'])
def editaStockProducte(request, pk):
    try:
        producte = Producte.objects.get(id=pk)
    except Producte.DoesNotExist:
        return Response({"error": "No existeix aquest producte."}, status=404)
    
    serializer = producteQuantSerializer(producte, data=request.data)
    if serializer.is_valid():
        serializer.save()  
        return Response({ "message:":" Stock del producte actualitzat", "data":serializer.data}, status=200)
    return Response({"error": "No s'ha pogut actualitzar la quantitat del producte", "data":serializer.errors}, status=400)