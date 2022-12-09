from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Farmer, Cart
from .serializers import FarmerSerializer, CartSerializer
@api_view(['GET'])
def getRoutes(request):

    routes = [
        {
            'Endpoint' : '/farmers',
            'method' : 'GET',
            'body' : None,
            'Description' : 'Returns array of farmers in db'
        },
        {
            'Endpoint' : '/farmers/id',
            'method' : 'GET',
            'body' : None,
            'Description' : 'Returns a single farmer with given id'
        },
        {
            'Endpoint' : '/farmers/create',
            'method' : 'POST',
            'body' : {'body' : ""},
            'Description' : 'Creates a new farmer with data sent'
        },
        {
            'Endpoint' : '/farmers/id/update',
            'method' : 'PUT',
            'body' : {'body' : ""},
            'Description' : 'Updates the entry farmer with given id in db'
        },
        {
            'Endpoint' : '/farmers/id/delete',
            'method' : 'DELETE',
            'body' : None,
            'Description' : 'Deletes the entry farmer with given id in db'
        },


    ]
    return Response(routes)

@api_view(['GET'])
def getAllFarmers(request):
    farmers = Farmer.objects.all()
    serializer = FarmerSerializer(farmers, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getFarmers(request, pk):
    farmer = Farmer.objects.get(id=pk)
    serializer = FarmerSerializer(farmer, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def createFarmer(request):
    data = request.data

    farmer = Farmer.objects.create(
        name = data['name'],
        address = data['address']
    )
    serializer = FarmerSerializer(farmer,many=False )
    return Response(serializer.data)

@api_view(['PUT'])
def updateFarmer(request,pk):
    data = request.data

    farmer = Farmer.objects.get(id=pk)
    serializer = FarmerSerializer(farmer,data = request.data )

    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['DELETE'])
def deleteFarmer(request,pk):
    farmer = Farmer.objects.get(id=pk)
    farmer.delete()
    return Response("Farmer was deleted")


@api_view(['POST'])
def createCart(request):
    data = request.data
    name = data['name']
    farmer = Farmer.objects.get(name=name)
    cart = Cart.objects.create(
        farmer=farmer,
        cart_holds=data['cart_holds'],
        name=name
    )
    serializer = CartSerializer(cart,many=False )
    return Response(serializer.data)

@api_view(['GET'])
def getAllCarts(request):
    carts = Cart.objects.all()
    serializer = CartSerializer(carts, many=True)
    return Response(serializer.data)