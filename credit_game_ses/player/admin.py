from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Car)
admin.site.register(House)
admin.site.register(Player)
admin.site.reigster(Choice)