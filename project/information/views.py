from django.shortcuts import render
from .serializers import FarmerPersonalDetailsSerializer, LandDetailsSerializer, LandPropertiesSerializer
from .models import FarmerPersonalDetails, LandProperties, LandDetails
from rest_framework.decorators import api_view
from rest_framework.response import Response

from django.http import HttpResponse
# Create your views here.
def homepage(request):
    return HttpResponse("Hi")


@api_view(['GET'])
def getAllFarmerPersonalDetails(request):
    farmers = FarmerPersonalDetails.objects.all()
    serializer = FarmerPersonalDetailsSerializer(farmers, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getAllLands(request):
    lands = LandDetails.objects.all()
    serializer = LandDetailsSerializer(lands, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getAllLandProperties(request):
    landProp = LandProperties.objects.all()
    serializer = LandPropertiesSerializer(landProp, many=True)
    return Response(serializer.data)

# @api_view(['GET'])
# def getAllFarmerNames(request):
#     print("In farmernames")
#     farmers = FarmerPersonalDetails.objects.all()
#     print(farmers)
#     data1 = getattr(farmers, "first_name")
#     print(data1)


#     serializer = FarmerPersonalDetailsSerializer(data1, many=True)
    
#     return Response(serializer.data)

@api_view(['POST'])
def createFarmerPersonalDetails(request):
    data = request.data

    farmer = FarmerPersonalDetails.objects.create(
        first_name = data['first_name'],
        last_name = data['last_name'],
        phone = data['phone'],
        gender = data['gender'],
        married = data['married'],
        dependent = data['dependent'],
        education = data['education'],
        self_employed = data['self_employed'],
        credit_history = data['credit_history'],
        loan_status = data['loan_status'],
        property_area = data['property_area'],
        # loan_id = data['loan_id'], #to be taken from backend later
        applicant_income = data['applicant_income'],
        coapplicant_income = data['coapplicant_income'],
        loan_amount = data['loan_amount'],
        loan_amount_term = data['loan_amount_term']

    )
    serializer = FarmerPersonalDetailsSerializer(farmer,many=False )
    return Response(serializer.data)

@api_view(['POST'])
def createLandDetails(request):
    data = request.data
    farmer_no = data['farmer_no']
    farmer = FarmerPersonalDetails.objects.get(id=farmer_no)
    land = LandDetails.objects.create(        
        farmer=farmer,
        farmer_no = farmer_no,
        address = data['address'],
        area = data['area'],        
        # length = data['length'],
        # breadth = data['breadth'],
        latitude = data['latitude'],
        longitude = data['longitude']

    )
    serializer = LandDetailsSerializer(land,many=False )
    return Response(serializer.data)

@api_view(['POST'])
def createLandProperties(request):
    data = request.data
    land_no = data['land_no']
    land = LandDetails.objects.get(id=land_no)
    landProp = LandProperties.objects.create(        
        land = land,
        land_no = data['land_no'],

        crop_marketibility = data['crop_marketibility'],
        crop_proposed = data['crop_proposed'],
        soil_fertility = data['soil_fertility'],
        enviromental_condition = data['enviromental_condition'],
        market_location = data['market_location'],
        water_arrangement = data['water_arrangement'],
        transport_system = data['transport_system'],
        storage_system = data['storage_system'],
        machinery_availability = data['machinery_availability'],
        manpower_availability = data['manpower_availability'],
        fertility_classification = data['fertility_classification'],
        farmer_repuation_locals = data['farmer_repuation_locals'],
        topography = data['topography'],
        seed_fertilizer_availability = data['seed_fertilizer_availability'],
        govt_subsidy_availability = data['govt_subsidy_availability'],
        technology_usage = data['technology_usage'],
        method_of_cultivation = data['method_of_cultivation'],


    )
    # land = LandDetails.objects.get(id = data['land_no'])
    # landProp=LandProperties(land=land)
    # landProp.save()
    serializer = LandPropertiesSerializer(landProp,many=False )
    return Response(serializer.data)