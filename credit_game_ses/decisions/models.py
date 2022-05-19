from django.db import models

# Create your models here.
class Decision(models.Model):
    name = models.TextField(max_length=100)
    description = models.TextField(max_length=255)
    effect = models.TextField(max_length=100)


class NumEffect(models.Model):  # I hated typing every character of these three classes, but I'm not sure how to do it better
    duration = models.IntegerField()
    value = models.IntegerField()
    description = models.TextField(max_length=255)

class HouseEffect(models.Model):
   duration = models.IntegerField()
   value = models.IntegerField()
   description = models.TextField(max_length=255)

class CarEffet(models.Model):
    duration = models.IntegerField()
    value = models.IntegerField()
    description = models.TextField(max_length=255)
