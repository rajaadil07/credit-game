from rest_framework import serializers
from .models import House,Car
 
class HouseSerializer(serializers.ModelSerializer):
    class Meta:
        model = House
        fields = "__all__"
 
class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = "__all__"