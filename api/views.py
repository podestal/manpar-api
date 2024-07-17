from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from . import serializers
from . import models

class DishViewSet(ModelViewSet):
    queryset = models.Dish.objects.all()
    serializer_class = serializers.GetDishSerializer

