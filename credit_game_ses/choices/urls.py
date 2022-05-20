from django.urls import path
from . import views

urlpatterns = [
    path('', views.overview, name='index'),
    path('random/', views.random_choices, name='choices'),
    path('decisions/', views.get_decisions, name='decisions'),
    path('decisions/', views.get_decisions, name='decisions'),
    path('effects/', views.effects, name='effects'),
]
