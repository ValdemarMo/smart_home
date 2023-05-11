from django.urls import path
from .views import CreateSensorView, UpdateSensorView, CreateMeasurementView, SensorListView, SensorIdView

urlpatterns = [
    path('sensors/create/', CreateSensorView.as_view(), name='create-sensor'),
    path('sensors/update/<pk>/', UpdateSensorView.as_view(), name='update-sensor'),
    path('measurements/create/', CreateMeasurementView.as_view(), name='create-measurement'),
    path('sensors/list/', SensorListView.as_view(), name='list-sensor'),
    path('sensors/<int:id>/', SensorIdView.as_view(), name='id-sensor'),
]


