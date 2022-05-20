from django.db import models
from choices.models import Effect


class Player(models.Model):
    #id = models.IntegerField(primary_key=True)
    name = models.CharField(default="",max_length=100)
    money = models.IntegerField(default=0)
    credit = models.IntegerField(default=0)
    interest = models.IntegerField(default=0)
    effects = models.ManyToManyField(Effect)


class House(models.Model):
    #id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.TextField()
    num_effect = models.ManyToManyField(Effect)
    user = models.ForeignKey(Player, on_delete=models.CASCADE)


class Car(models.Model):
    #id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.TextField()
    effects = models.ManyToManyField(Effect)
    user = models.ForeignKey(Player, on_delete=models.CASCADE)
