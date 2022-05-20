from django.shortcuts import render, HttpResponse
from django.http import HttpResponse, HttpResponseNotAllowed
from .forms import PlayerInfo
from .serializers import HouseSerializer, CarSerializer
from .models import House, Car, Player

from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.


def player_information(request):
    if request.method == "POST":
        player_form = PlayerInfo(request.POST)
        if player_form.is_valid():
            player_form.save()

    player_form = PlayerInfo()

    return render(request, 'player/player_info.html', {'form': player_form})


@api_view(['GET', 'POST'])
def api_overview(request):
    return Response("API Base Point", safe=False)


@api_view(['GET', 'POST'])
def houseList(request):
    houses = House.objects.all()
    serializer = HouseSerializer(houses, many=True)
    return Response(serializer.data)


@api_view(['GET', 'POST'])
def carList(request):
    cars = Car.objects.all()
    serializer = CarSerializer(cars, many=True)
    return Response(serializer.data)


def increment(request):
    if request.method != "PATCH":
        return HttpResponseNotAllowed(["PATCH"])

    player = Player.objects.get(id=request.GET.get("id"))

    player.age += 1
    player.money += int(player.money * player.interest / 100)

    if len(player.effects.all()) is 0:
        player.save()
        return HttpResponse("OK")

    for effect in player.effects.all():
        if effect.effect_type == "money":
            player.money += effect.value
        elif effect.effect_type == "credit":
            player.credit += effect.value
        effect.duration -= 1

    player.save()
    return HttpResponse("OK")
