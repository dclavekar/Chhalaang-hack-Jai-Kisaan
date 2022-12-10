from rest_framework.serializers import ModelSerializer
from .models import FarmerPersonalDetails, LandDetails

class FarmerPersonalDetailsSerializer(ModelSerializer):
    class Meta:
        model = FarmerPersonalDetails
        fields = '__all__'

class LandDetailsSerializer(ModelSerializer):
    class Meta:
        model = LandDetails
        fields = '__all__'