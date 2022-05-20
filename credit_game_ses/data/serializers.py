from rest_framework import serializers
from .models import *


class HouseSerializer(serializers.ModelSerializer):
    class Meta:
        model = House
        fields = "__all__"


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = "__all__"


class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = "__all__"
