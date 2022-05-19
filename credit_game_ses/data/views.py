from django.http import HttpResponseNotAllowed, HttpResponse
from django.shortcuts import render
from .forms import PlayerInfo
from .models import Player
from math import floor

# Create your views here.


def player_information(request):
    if request.method == "POST":
        player_form = PlayerInfo(request.POST)
        if player_form.is_valid():
            player_form.save()

    player_form = PlayerInfo()

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
        if effect.type == "money":
            player.money += effect.value
        elif effect.type == "credit":
            player.credit += effect.value
        effect.duration -= 1

    player.save()
    return HttpResponse("OK")
