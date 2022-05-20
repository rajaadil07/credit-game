from tkinter import W
from django.shortcuts import render, redirect, HttpResponse
from django.http import HttpResponse, HttpResponseNotAllowed, JsonResponse
from .forms import *
from .serializers import *
from .models import House, Car, Player

from rest_framework.decorators import api_view
from rest_framework.response import Response


def thank_you(request):
    return render(request, 'player/thank_you.html')


def player_information(request):
    if request.method == "POST":
        player_form = PlayerInfo(request.POST)
        if player_form.is_valid():
            player_data = player_form.save()
            player_id = player_data.id

            return redirect('stats-upload', id=player_id)

    player_form = PlayerInfo()

    return render(request, 'player/player_info.html', {'form': player_form})


def player_stats(request, id):
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

            return redirect('thank-you')

    house_form = HouseInfo()
    car_form = CarInfo()

    return render(request, 'player/player_stats.html', {'house_form': house_form, 'car_form': car_form})


@api_view(['GET', 'POST'])
def api_overview(request):
    players = Player.objects.all()
    serializer = PlayerSerializer(players, many=True)
    return JsonResponse(serializer.data, safe=False)


@api_view(['GET', 'POST'])
def houseList(request):
    houses = House.objects.all()
    serializer = HouseSerializer(houses, many=True)
    return JsonResponse(serializer.data, safe=False)


@api_view(['GET', 'POST'])
def carList(request):
    cars = Car.objects.all()
    serializer = CarSerializer(cars, many=True)
    return JsonResponse(serializer.data, safe=False)


def increment(request):
    if request.method != "PATCH":
        return HttpResponseNotAllowed(["PATCH"])

    player = Player.objects.get(id=request.GET.get("id"))

    player.age += 1
    player.money += int(player.money * player.interest / 100)
    player.money += 1000

    if len(player.effects.all()) is 0:
        player.save()
        return HttpResponse("OK")

    for effect in player.effects.all():
        if effect.effect_type == "money":
            player.money += effect.value
        elif effect.effect_type == "credit":
            player.credit += effect.value
        elif effect.effect_type == "interest":
            player.interest += effect.value
        elif effect.effect_type == "house":
            player.house.set(House.objects.get(id=effect.value))
        elif effect.effect_type == "car":
            player.car.set(Car.objects.get(id=effect.value))

        effect.duration -= 1

    player.save()
    return HttpResponse("OK")
