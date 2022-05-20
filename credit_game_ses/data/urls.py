from django.urls import path
from . import views

urlpatterns = [
    path('playerInfo', views.player_information, name='player-info'),
    path('api', views.api_overview, name="api-overview"),
    path('house-list/', views.houseList, name="house-list"),
    path('car-list/', views.carList, name="car-list"),
    path('increment/', views.increment, name="increment"),
    path('stats-upload/<int:id>/', views.player_stats,name='stats-upload'),
    path('thank-you/',views.thank_you, name='thank-you'),

]
