from .models import *
from django import forms


class PlayerInfo(forms.ModelForm):
    name = forms.CharField(max_length=100)
    age = forms.IntegerField()
    credit_score = forms.IntegerField()
    money = forms.IntegerField()
    interest = forms.IntegerField()

    class Meta:
        model = Player
        fields = ['name','age','credit_score','money','interest']


class HouseInfo(forms.ModelForm):
    house_name = forms.CharField(max_length=100)
    house_description = forms.CharField(max_length=255)

    class Meta:
        model = House
        fields = ['house_name', 'house_description']


class CarInfo(forms.ModelForm):
    car_name = forms.CharField(max_length=100)
    car_description = forms.CharField(max_length=255)

    class Meta:
        model = Car
        fields = ['car_name', 'car_description']
