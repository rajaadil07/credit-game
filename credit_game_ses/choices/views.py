from django.shortcuts import render
from random import randint
from .models import Choice, Decision, Effect
from choices.serializers import ChoiceSerializer, DecisionSerializer, EffectSerializer
from rest_framework import viewsets


class ChoiceViewSet(viewsets.ModelViewSet):
    queryset = Choice.objects.all()
    serializer_class = ChoiceSerializer


class DecisionViewSet(viewsets.ModelViewSet):
    queryset = Decision.objects.all()
    serializer_class = DecisionSerializer


class EffectViewSet(viewsets.ModelViewSet):
    queryset = Effect.objects.all()
    serializer_class = EffectSerializer


def getChoice(request):
    possible_choices = Choice.objects.all()
    num_choices = randint(1, 3)
    choices = []

    for i in range(num_choices):
        choices.append(possible_choices[randint(0, len(possible_choices) - 1)])
