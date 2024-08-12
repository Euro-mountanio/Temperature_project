from django.db import models

class TemperatureReading(models.Model):
    temperature = models.FloatField()

