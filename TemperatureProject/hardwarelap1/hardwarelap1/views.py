from django.http import JsonResponse
from django.shortcuts import render

from .model import TemperatureReading

def show_temp(request):
    # Fetch the latest temperature reading (or all readings)
    latest_reading = TemperatureReading.objects.order_by('-id').first()
    # You can also fetch all readings using TemperatureReading.objects.all()

    return render(request, 'home.html', {'api_data': latest_reading})