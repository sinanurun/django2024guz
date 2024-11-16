from django.http import JsonResponse
from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from product.models import Product
from productapi.serializers import ProductSerializer


# Create your views here.
@api_view(['GET'])
def index(request):
    # adım 1
    # products = Product.objects.all()
    # print(products)
    # products_list = list(products.values())
    # print(products_list)
    # return JsonResponse({'products': products_list})
    # # adım2
    # products = Product.objects.all()
    # serializer = ProductSerializer(products, many=True)
    # return JsonResponse(serializer.data, safe=False)
    # adım3
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_product(request,id):
    try:
        product = Product.objects.get(pk = id)
        serializer = ProductSerializer(product)
        return Response(serializer.data)
    except Product.DoesNotExist as e:
        return Response({'error':f'Product bulunamadı {e}'},
                        status=status.HTTP_404_NOT_FOUND)

@api_view(['GET','DELETE'])
def delete_product(request,id):
    try:
        product = Product.objects.get(pk = id)
        product.delete()
        return Response({'message':'Product silindi'}, status=status.HTTP_204_NO_CONTENT)
    except Product.DoesNotExist as e:
        return Response({'error': f'Product bulunamadı {e}'},
                        status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
def create_product(request):
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def update_product(request, id):
    product = Product.objects.get(pk=id)
    serializer = ProductSerializer(product, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)