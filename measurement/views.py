from django.shortcuts import render
from rest_framework.decorators import api_view


# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
# Создать датчик. Указываются название и описание датчика.
# Изменить датчик. Указываются название и описание.
# Добавить измерение. Указываются ID датчика и температура.
# Получить список датчиков. Выдаётся список с краткой информацией по датчикам: ID, название и опис


@api_view
def