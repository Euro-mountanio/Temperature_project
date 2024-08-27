from django.http import JsonResponse
from ninja import Router, Schema, NinjaAPI
from pydantic import ConfigDict
from .models import TemperatureReading, HumidityReading


api = NinjaAPI()


class TemperatureReadingSchema(Schema):
    temperature: float
    humidity: float



@api.post("/temperature")
def create_temperature_reading(request, temperature_data: TemperatureReadingSchema):
    reading_temperature = TemperatureReading(temperature=temperature_data.temperature)
    reading_temperature.save()
    reading_humidity = HumidityReading(humidity=temperature_data.humidity)
    reading_humidity.save()
    return 0


@api.get("/show")
def show_temp(request , temp_data: TemperatureReadingSchema):
    data = temp_data.temperature
    return f"temperature {data}"


@api.get("/hello")
def hello(request, name=" world "):
    return f"hello  {name}"

@api.get("/show_temperature")
def show_temp(request):
    temperature_reading = TemperatureReading.objects.order_by('-id').first()
    humidity_reading = HumidityReading.objects.order_by('-id').first()
    data = {
        "temperature": temperature_reading.temperature,
        "humidity": humidity_reading.humidity
    }
    return data







