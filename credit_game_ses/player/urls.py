from django.urls import path
from . import views

urlpatterns = [
    path('playerInfo',views.player_information,name='player-info'),
]