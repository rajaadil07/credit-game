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
    name = forms.CharField(max_length=100)
    description = forms.CharField(max_length=255)

    class Meta:
        model = House
        fields = ['name', 'description']


class CarInfo(forms.ModelForm):
    name = forms.CharField(max_length=100)
    description = forms.CharField(max_length=255)

    class Meta:
        model = Car
        fields = ['name', 'description']
