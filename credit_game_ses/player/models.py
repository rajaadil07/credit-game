from django.db import models
from django.contrib.postgres.fields import ArrayField

# Create your models here.
class Car(models.Model):
    name = models.IntegerField()
    price = models.FloatField()
    description = models.TextField(max_length=255)

class House(models.Model):
    cost = models.FloatField()
    description = models.TextField(max_length=255)

class Player(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age = models.IntegerField()
    credit_score = models.IntegerField()
    money = models.FloatField()
    house = models.ForeignKey(House, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    effects = ArrayField(ArrayField(models.IntegerField()))

class Choice(models.Model):
    name = models.CharField(max_length=255)
    price = models.TextField(max_length=100)
    decisions = ArrayField(ArrayField(models.IntegerField()))
