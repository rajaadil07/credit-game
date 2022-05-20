from django.urls import path
from . import views

urlpatterns = [
    path('playerInfo', views.player_information, name='player-info'),
    path('api', views.api_overview, name="api-overview"),
    path('house-list/', views.houseList, name="house-list"),
    path('car-list/', views.carList, name="car-list"),
    path('increment/', views.increment, name="increment"),
]
