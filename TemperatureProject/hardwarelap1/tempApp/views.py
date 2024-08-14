from django.http import JsonResponse
from django.shortcuts import render

from .models import TemperatureReading, HumidityReading

def show_temp(request):
    # Fetch the latest temperature reading (or all readings)
    temperature_reading = TemperatureReading.objects.order_by('-id').first()
    humidity_reading = HumidityReading.objects.order_by('-id').first()

    # You can also fetch all readings using TemperatureReading.objects.all()
    return render(request, 'index.html', {'temp_data': temperature_reading, 'humidity_data': humidity_reading})