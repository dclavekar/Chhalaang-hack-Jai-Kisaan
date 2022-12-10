from django.shortcuts import render
from .serializers import FarmerPersonalDetailsSerializer, LandDetailsSerializer
from .models import FarmerPersonalDetails, LandDetails
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.template import loader

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

    # ls=

    land = LandDetails.objects.create(        
        farmer=farmer,
        farmer_no = farmer_no,
        address=data['address'],
        area_given=data['area_given'],
        # area_calculated=data['area_calculated'],





        cordinate1_x=data['cordinate1_x'],
        cordinate1_y=data['cordinate1_y'],
        cordinate2_x=data['cordinate2_x'],
        cordinate2_y=data['cordinate2_y'],
        cordinate3_x=data['cordinate3_x'],
        cordinate3_y=data['cordinate3_y'],
        cordinate4_x=data['cordinate4_x'],
        cordinate4_y=data['cordinate4_y'],
        n=data['n'],
        # soil_image=data['soil_image'],
        # crop_image=data['crop_image'],        

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
def fun(request):
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
    
    # template = loader.get_template('trial.html')
    # context = {
    
    # 'variable':"heeeeeee"
    
    # }
    # return render(request,'geolocation.html', {'cordinate_matrix': "l", })#change to l
    return HttpResponse(template.render(context, request))
    # return HttpResponse("done")


