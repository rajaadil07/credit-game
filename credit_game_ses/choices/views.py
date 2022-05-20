from django.shortcuts import render
from random import randint
from .models import Choice, Decision, Effect
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ChoiceSerializer, DecisionSerializer, EffectSerializer


def get_choices(request):
    possible_choices = Choice.objects.all()
    num_choices = randint(1, 3)
    choices = []

    for i in range(num_choices):
        choices.append(possible_choices[randint(0, len(possible_choices) - 1)])


@api_view(['GET'])
def overview(request):
    choices = Choice.objects.all()
    serializer = ChoiceSerializer(choices, many=True)
    return Response(serializer.data)
