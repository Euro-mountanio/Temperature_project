from django.contrib import admin

from .models import TemperatureReading, HumidityReading

# Register your models here.

admin.site.register(TemperatureReading)
admin.site.register(HumidityReading)