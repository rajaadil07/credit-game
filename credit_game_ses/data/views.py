from django.http import HttpResponseNotAllowed, HttpResponse
from django.shortcuts import render
from .forms import *
from .models import Player
from math import floor

# Create your views here.


def player_information(request):
    if request.method != "POST":
        return HttpResponseNotAllowed(["POST"])

    player_form = PlayerInfo(request.POST)
    house_form = HouseInfo(request.POST)
    car_form = CarInfo(request.POST)
    if player_form.is_valid() and house_form.is_valid() and car_form.is_valid():
        player_form.save()
        house_form.save(commit=False)
        car_form.save(commit=False)
        id = request.get_clean_data()["id"]

    player_form = PlayerInfo()
    print(player_form, house_form, car_form)
    return render(request, 'player/player_info.html', {'form': player_form})


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
