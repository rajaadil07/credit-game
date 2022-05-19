from django.db import models
from django.contrib.postgres.fields import ArrayField


class Effect(models.Model):
    duration = models.IntegerField()
    value = models.IntegerField()
    description = models.TextField(max_length=255)
    type = models.CharField(max_length=20)


class Decision(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=255)
    effect = models.ForeignKey(Effect, on_delete=models.CASCADE)


class Choice(models.Model):
    description = models.CharField(max_length=200)
    decisions = models.ManyToManyField(Decision)
