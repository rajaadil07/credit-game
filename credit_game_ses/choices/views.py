from django.shortcuts import render
from random import randint
from .models import Choice, Decision, Effect
from django.http import JsonResponse, HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ChoiceSerializer, DecisionSerializer, EffectSerializer


@api_view(['GET'])
def random_choices(request):
    possible_choices = Choice.objects.all()
    num_choices = randint(1, 4)
    index_choices = []

    for i in range(num_choices):
        choice = randint(0, len(possible_choices) - 1)
        index_choices.append(choice)

    choices = possible_choices.filter(id__in=index_choices)
    serializer = ChoiceSerializer(choices, many=True)
    return JsonResponse(serializer.data, safe=False)


@api_view(['GET'])
def get_decisions(request):

    decisions = Decision.objects.all()
    serializer = DecisionSerializer(decisions, many=True)
    return JsonResponse(serializer.data, safe=False)


@api_view(['GET'])
def overview(request):
    choices = Choice.objects.all()
    serializer = ChoiceSerializer(choices, many=True)
    return JsonResponse(serializer.data, safe=False)


@api_view(['GET'])
def effects(request):
    effects = Effect.objects.all()
    serializer = EffectSerializer(effects, many=True)
    return JsonResponse(serializer.data, safe=False)
