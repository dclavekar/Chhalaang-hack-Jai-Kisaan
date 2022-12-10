from django.shortcuts import render
from .serializers import FarmerPersonalDetailsSerializer, LandDetailsSerializer
from .models import FarmerPersonalDetails, LandDetails
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.template import loader

from django.http import HttpResponse
# Create your views here.
def homepage(request):
    return render(request, 'welcome.html')

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



@api_view(['POST'])
def createFarmerPersonalDetails(request):
    data = request.data

    farmer = FarmerPersonalDetails.objects.create(
        first_name = data['first_name'],
        last_name = data['last_name'],
        phone = data['phone'],

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
        address=data['address'],
        area_given=data['area_given'],
        cordinate1_x=data['cordinate1_x'],
        cordinate1_y=data['cordinate1_y'],
        cordinate2_x=data['cordinate2_x'],
        cordinate2_y=data['cordinate2_y'],
        cordinate3_x=data['cordinate3_x'],
        cordinate3_y=data['cordinate3_y'],
        cordinate4_x=data['cordinate4_x'],
        cordinate4_y=data['cordinate4_y'],
        n=data['n'],
              

    )
    serializer = LandDetailsSerializer(land,many=False )
    return Response(serializer.data)


def geolocation_map_rendering(request,land):

    cordinate1_x=land.cordinate1_x
    cordinate1_y=land.cordinate1_y
    cordinate2_x=land.cordinate2_x
    cordinate2_y=land.cordinate2_y
    cordinate3_x=land.cordinate3_x
    cordinate3_y=land.cordinate3_y
    cordinate4_x=land.cordinate4_x
    cordinate4_y=land.cordinate4_y

    
    l=[[cordinate1_x, cordinate1_y],[cordinate2_x, cordinate2_y],[cordinate3_x, cordinate3_y],[cordinate4_x, cordinate4_y]]
    # ls=[l,cordinate1_x,cordinate1_y]
    return l

@api_view(['POST'])
def get_geolocation(request):
    data = request.data
    land_no = data['land_no']
    land = LandDetails.objects.get(id=land_no)  
    l=geolocation_map_rendering(request,land)
    template = loader.get_template('geolocation.html')
    context = {    
    'cordinate1_x':l[0][0],
    'cordinate1_y':l[0][1],
    'cordinate2_x':l[1][0],
    'cordinate2_y':l[1][1],
    'cordinate3_x':l[2][0],
    'cordinate3_y':l[2][1],
    'cordinate4_x':l[3][0],
    'cordinate4_y':l[3][1],      
    }

    return HttpResponse(template.render(context, request))


@api_view(['POST'])
def get_images(request):
    data = request.data
    soil_img_byte = data['soil_img_byte']
    soil_img_src = "data:image/png;base64,"+ soil_img_byte

    crop_img_byte = data['crop_img_byte']
    crop_img_src = "data:image/png;base64,"+ crop_img_byte

    template = loader.get_template('soil.html')
    context = {    
    'soil_img_src':soil_img_src,
    'crop_img_src':crop_img_src,
    }    
    return HttpResponse(template.render(context, request))

@api_view(['GET'])
def all_details_report(request, primary_key):
    farmers=LandDetails.objects.get(id=primary_key)  
    context={'details' : farmers,}
    return render(request, 'report.html', context)
