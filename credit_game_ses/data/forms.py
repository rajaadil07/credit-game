from .models import Player
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
