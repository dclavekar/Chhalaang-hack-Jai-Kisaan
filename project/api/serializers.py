from rest_framework.serializers import ModelSerializer
from .models import Farmer, Cart

class FarmerSerializer(ModelSerializer):
    class Meta:
        model = Farmer
        fields = '__all__'

        
class CartSerializer(ModelSerializer):
    class Meta:
        model = Cart
        fields = '__all__'