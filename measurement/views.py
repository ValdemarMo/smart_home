from django.shortcuts import render

from rest_framework.generics import CreateAPIView, ListAPIView, UpdateAPIView, CreateAPIView, RetrieveAPIView
from measurement.models import Sensor, Measurement
from measurement.serializers import SensorSerializer, MeasurementSerializer, SensorListSerializer


class CreateSensorView(CreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer

class UpdateSensorView(UpdateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer

class CreateMeasurementView(CreateAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer

class SensorListView(ListAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorListSerializer

class SensorIdView(RetrieveAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer
    lookup_field = 'id'