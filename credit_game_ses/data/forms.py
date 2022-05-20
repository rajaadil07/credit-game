from .models import *
from django import forms


class PlayerInfo(forms.ModelForm):
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    age = forms.IntegerField()
    credit_score = forms.IntegerField()
    money = forms.IntegerField()
    interest = forms.IntegerField()

    class Meta:
        model = Player
        fields = ['first_name', 'last_name', 'age',
                  'credit_score', 'interest', 'money']


class HouseInfo(forms.ModelForm):
    name = forms.CharField(max_length=100)
    description = forms.IntegerField()
    num_effect = forms.IntegerField()
    user = forms.IntegerField()

    class Meta:
        model = House
        fields = ['name', 'description', 'num_effect', 'user']


class CarInfo(forms.ModelForm):
    name = forms.CharField(max_length=100)
    description = forms.IntegerField()
    effects = forms.IntegerField()
    user = forms.IntegerField()

    class Meta:
        model = Car
        fields = ['name', 'description', 'effects', 'user']
