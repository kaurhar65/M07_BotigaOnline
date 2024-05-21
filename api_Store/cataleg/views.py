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