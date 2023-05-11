from django.db import models

class Sensor(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=100, default=None)

class Measurement(models.Model):
    sensor = models.ForeignKey('Sensor', related_name='measurements', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    temperature = models.DecimalField(max_digits=5, decimal_places=2)
    # image = models.ImageField(null=True)

