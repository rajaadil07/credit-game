from django.shortcuts import render
from .forms import PlayerInfo

# Create your views here.
def player_information(request):
    if request.method == "POST":
        player_form = PlayerInfo(request.POST)
        if player_form.is_valid():
            player_form.save()

    player_form = PlayerInfo()

    return render(request,'player/player_info.html', {'form': player_form})