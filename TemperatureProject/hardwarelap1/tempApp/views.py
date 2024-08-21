import json
from datetime import datetime

from django.http import JsonResponse
from django.shortcuts import render
from django.core import serializers

from .models import TemperatureReading, HumidityReading



def show_temp(request):
    # Fetch the latest temperature reading (or all readings)
    temperature_reading = TemperatureReading.objects.order_by('-id').first()
    humidity_reading = HumidityReading.objects.order_by('-id').first()

    first_6_temp = []
    temp_timestamp = []
    t = TemperatureReading.objects.order_by('-id')[:6]
    for element in t:
        first_6_temp.append(element.temperature)
        temp_timestamp.append(element.timestamp )
    first_6_hum = []
    hum_timestamp = []
    h = HumidityReading.objects.order_by('-id')[:6]
    for element in h:
        first_6_hum.append(element.humidity)
        hum_timestamp.append(element.timestamp)


    # You can also fetch all readings using TemperatureReading.objects.all()
    return render(request, 'index.html', {'temp_data': temperature_reading, 'humidity_data': humidity_reading, 'temp':first_6_temp, 'hum': first_6_hum , 'temp_timestamp': temp_timestamp, 'hum_timestamp': hum_timestamp})

def chart(request):
   # temperature_data = serializers.serialize(TemperatureReading.objects.all(),any)
    #humidity_data = serializers.serialize(HumidityReading.objects.all(),any )

    return render(request, 'home.html', )


