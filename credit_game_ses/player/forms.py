from .models import Player
from django import forms

class PlayerInfo(forms.ModelForm):
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    age = forms.IntegerField(max_length=150)
    credit_score = forms.IntegerField()
    money = forms.FloatField()

    class Meta:
        model = Player
        fields = ['first_name','last_name','age','credit_score','money']