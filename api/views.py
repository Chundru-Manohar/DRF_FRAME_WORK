from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .serializer import ProductSeralizer
from .models import Product
# Create your views here.
@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'List':'/product-list/',
        'Detail view':'/product-detail/<int:id>',
        'create':'/product-create/',
        'update':'/product-update/<int:id>',
        'delete':'/product-delete/<int:id>',
    }

    return Response(api_urls);

@api_view(['GET'])
def showall(request):
    products = Product.objects.all()
    seral = ProductSeralizer(products,many=True)
    return Response(seral.data)


@api_view(['GET'])
def ViewProduct(request,pk):
    products = Product.objects.get(id=pk)
    seral = ProductSeralizer(products,many=False)
    return Response(seral.data)

@api_view(['POST'])
def createProduct(request):
    seral = ProductSeralizer(data = request.data)
    if seral.is_valid():
        seral.save()
    return Response(seral.data)


@api_view(['POST'])
def updateProduct(request,pk):
    products = Product.objects.get(id=pk)
    seral = ProductSeralizer(instance=products,data = request.data)
    if seral.is_valid():
        seral.save()
    return Response(seral.data)

@api_view(['GET'])
def deleteProduct(request,pk):
    products = Product.objects.get(id=pk)
    products.delete()
    return Response("iteam deleted sucessfully")
