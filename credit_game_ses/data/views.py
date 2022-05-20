from django.shortcuts import render, redirect, HttpResponse
from django.http import HttpResponse, HttpResponseNotAllowed
from .forms import *
from .serializers import HouseSerializer, CarSerializer
from .models import House, Car, Player

from rest_framework.decorators import api_view
from rest_framework.response import Response

def player_information(request):
    if request.method == "POST":
        player_form = PlayerInfo(request.POST)
        if player_form.is_valid():
            player_data = player_form.save()
            player_id = player_data.id

            return redirect('stats-upload', id=player_id)

    player_form = PlayerInfo()

    return render(request, 'player/player_info.html', {'form': player_form})

def player_stats(request,id): 
    if request.method == "POST":
        house_form = HouseInfo(request.POST)
        car_form = CarInfo(request.POST)
        if house_form.is_valid() and car_form.is_valid():
            house_instance = house_form.save(commit=False)
            car_instance = car_form.save(commit=False)

            house_instance.user = Player.objects.get(pk=id)
            car_instance.user = Player.objects.get(pk=id)
            house_instance.save()
            car_instance.save()

            return redirect('player-info')

    house_form = HouseInfo()
    car_form = CarInfo()

    return render(request, 'player/player_stats.html', {'house_form': house_form, 'car_form': car_form})


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
