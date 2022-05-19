from django.db import models
from choices.models import Effect


class House(models.Model):
    name = models.CharField(max_length=100)
    description = models.IntegerField()
    num_effect = models.ForeignKey(Effect, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Car(models.Model):
    name = models.CharField(max_length=100)
    description = models.IntegerField()
    num_effect = models.ForeignKey(Effect, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Player(models.Model):
    name = models.CharField(max_length=100)
    money = models.IntegerField()
    credit = models.IntegerField(max_length=850)
    house = models.ForeignKey(House, on_delete=models.CASCADE)
    interest = models.IntegerField(max_length=255)
